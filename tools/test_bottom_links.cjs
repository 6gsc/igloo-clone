const assert = require('node:assert/strict');
const fs = require('node:fs');
const pw = require(process.env.PLAYWRIGHT_ROOT || `${process.env.HOME}/.npm/_npx/f0a362733743bae2/node_modules/playwright`);
const url = process.argv[2] || 'http://127.0.0.1:8791/';
const artifacts = process.argv[3] || '/Users/inoplanet/Desktop/个人经验/igloo-clone/shots';

(async () => {
  fs.mkdirSync(artifacts, { recursive: true });
  const browser = await pw.chromium.launch();
  try {
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 } });
    await context.grantPermissions(['clipboard-read', 'clipboard-write'], { origin: new URL(url).origin });
    const page = await context.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(`pageerror: ${e.message}`));
    page.on('console', m => {
      if (m.type() === 'error' || m.text().includes('not present in the MSDF')) {
        errors.push(`console(${m.type()}): ${m.text()}`);
      }
    });

    await page.route('**/App3D-form-a-v6.js', async r => {
      const response = await r.fetch();
      const source = await response.text();
      const jFPattern = /class jF\{constructor\(e\)\{this\.options=e/;
      assert.match(source, jFPattern);
      const patched = source.replace(jFPattern, 'class jF{constructor(e){window.scrollCtrlForTest=this;this.options=e');
      return r.fulfill({ response, body: patched });
    });

    await page.goto(url, { waitUntil: 'networkidle' });
    await page.waitForFunction(() => Boolean(window.scrollCtrlForTest), {}, { timeout: 45000 });
    await page.waitForTimeout(1200);

    // Jump cleanly into the bottom entry scene resting link carousel
    await page.evaluate(() => {
      const sc = window.scrollCtrlForTest;
      const iglooH = sc.scrollComposers[0].passes[0].scene.height;
      const cubesH = sc.scrollComposers[1].passes[0].scene.height;
      const entryScene = sc.scrollComposers[2].passes[0].scene;
      const targetY = iglooH + cubesH + entryScene.height * entryScene.finalScrollAutocenter;
      sc.scroll.targetY1 = targetY;
      sc.scroll.targetY2 = targetY;
      sc.scroll.y = targetY;
    });
    await page.waitForTimeout(2500);

    const checkState = () => page.evaluate(() => {
      const entry = window.scrollCtrlForTest.scrollComposers[2].passes[0].scene;
      const wF = entry.containerparticles;
      const xF = wF.UI?.bottom;
      return {
        entryProgress: Number(entry.progress.toFixed(3)),
        currentLink: wF.currentLink,
        uiEnabled: Boolean(wF.UI?.enabled),
        titlesCount: xF?.texts?.group?.children?.length || 0,
        isCopied: Boolean(xF?.texts?._isCopied),
        hintVisible: Boolean(xF?.texts?.hintGroup?.visible),
        bottomY: xF?.bottomPosition || 0,
      };
    });

    // Slide 1: 邮箱联系 (mail_64) — verify info line is visible & clicking center icon copies email
    await page.keyboard.press('ArrowRight');
    await page.waitForTimeout(2200);
    const s1 = await checkState();
    await page.screenshot({ path: `${artifacts}/plan-a-02-mail.png` });
    await page.mouse.click(720, 440);
    await page.waitForTimeout(700);
    const s1Copied = await checkState();
    const mailClip = await page.evaluate(() => navigator.clipboard.readText());

    // Slide 2: 电话/微信 (phone_wechat_64) resting state
    await page.keyboard.press('ArrowRight');
    await page.waitForTimeout(2200);
    const s2Idle = await checkState();
    await page.screenshot({ path: `${artifacts}/plan-a-03-phone-idle.png` });

    // Click the bottom [ 电话/微信 ] button to test one-click clipboard copy + MSDF feedback
    await page.mouse.click(720, s2Idle.bottomY);
    await page.waitForTimeout(700);
    const s2Copied = await checkState();
    const clipboardText = await page.evaluate(() => navigator.clipboard.readText());
    await page.screenshot({ path: `${artifacts}/plan-a-03-phone-copied.png` });

    // Slide 0: 个人简历 (cv_doc_64) — verify info line is visible & clicking center icon opens/requests PDF
    await page.keyboard.press('ArrowRight');
    await page.waitForTimeout(2200);
    const s0 = await checkState();
    await page.screenshot({ path: `${artifacts}/plan-a-01-resume.png` });
    const openedUrls = [];
    await page.evaluate(() => {
      window.__openedForTest = [];
      const origOpen = window.open.bind(window);
      window.open = (u, t) => { window.__openedForTest.push(u); return origOpen(u, t); };
    });
    const popupPromise = page.waitForEvent('popup', { timeout: 3000 }).catch(() => null);
    await page.mouse.click(720, 440);
    const popup = await popupPromise;
    await page.waitForTimeout(500);
    const s0Opened = await checkState();
    const openedList = await page.evaluate(() => window.__openedForTest || []);
    if (popup) await popup.close().catch(() => {});

    const pdfStatus = await page.evaluate(async () => {
      const res = await fetch('./assets/resume-guishaocong.pdf', { method: 'HEAD' });
      return { status: res.status, type: res.headers.get('content-type') };
    });

    console.log(JSON.stringify({ s0, s0Opened, openedList, s1, s1Copied, mailClip, s2Idle, s2Copied, clipboardText, pdfStatus, errors }, null, 2));
    assert.deepEqual(errors, []);
    assert.equal(s0.currentLink, 0);
    assert.equal(s0.hintVisible, true);
    assert.equal(s0Opened.currentLink, 0);
    assert.equal(s0Opened.isCopied, true);
    assert.deepEqual(openedList, ['./assets/resume-guishaocong.pdf']);
    assert.equal(s1.currentLink, 1);
    assert.equal(s1.hintVisible, true);
    assert.equal(s1Copied.currentLink, 1);
    assert.equal(s1Copied.isCopied, true);
    assert.equal(mailClip, 'EurusGui@qq.com');
    assert.equal(s2Idle.currentLink, 2);
    assert.equal(s2Idle.hintVisible, true);
    assert.equal(s2Idle.isCopied, false);
    assert.equal(s2Copied.currentLink, 2);
    assert.equal(s2Copied.isCopied, true);
    assert.equal(clipboardText, '18504205236');
    assert.equal(pdfStatus.status, 200);
  } finally {
    await browser.close();
  }
})();
