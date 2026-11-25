const assert = require('node:assert/strict');
const fs = require('node:fs');
const pw = require(process.env.PLAYWRIGHT_ROOT || `${process.env.HOME}/.npm/_npx/f0a362733743bae2/node_modules/playwright`);
const url = process.argv[2] || 'http://127.0.0.1:8791/';
const artifacts = process.argv[3] || '/Users/inoplanet/Desktop/个人经验/igloo-clone/shots';

(async () => {
  fs.mkdirSync(artifacts, { recursive: true });
  const browser = await pw.chromium.launch();
  try {
    const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    page.on('console', m => {
      if (m.type() === 'error' || m.text().includes('not present in the MSDF')) errors.push(m.text());
    });
    await page.route('**/App3D-form-a-v6.js', async r => {
      const response = await r.fetch();
      const source = await response.text();
      const pattern = /async init\(\)\{const e=await zt\.batched\("igloo\.drc"\)/;
      assert.match(source, pattern);
      return r.fulfill({
        response,
        body: source.replace(pattern, match => match.replace('const e=', 'window.heroForTest=this;const e='))
      });
    });

    await page.goto(url, { waitUntil: 'networkidle' });
    await page.mouse.move(10, 880);
    await page.waitForFunction(() => window.heroForTest?.scene.introTL?.progress() === 1, {}, { timeout: 45000 });
    await page.waitForTimeout(1800);

    // 1. Desktop resting state
    await page.screenshot({ path: `${artifacts}/form-a-01-rest.png` });

    // 2. Hover Q0 (top-left quadrant)
    await page.evaluate(() => { window.heroForTest._lockHover = 0; });
    await page.mouse.move(460, 420, { steps: 10 });
    await page.waitForTimeout(700);
    await page.screenshot({ path: `${artifacts}/form-a-02-hover-q0.png` });

    // 3. Hover Q1 (top-right quadrant)
    await page.evaluate(() => { window.heroForTest._lockHover = 1; });
    await page.mouse.move(980, 420, { steps: 10 });
    await page.waitForTimeout(700);
    await page.screenshot({ path: `${artifacts}/form-a-03-hover-q1.png` });

    // 4. Release lock and test mid-scroll particle burst
    await page.evaluate(() => { window.heroForTest._lockHover = null; });
    await page.mouse.move(720, 450);
    for (let k = 0; k < 5; k++) {
      await page.mouse.wheel(0, 260);
      await page.waitForTimeout(90);
    }
    await page.waitForTimeout(350);
    await page.screenshot({ path: `${artifacts}/form-a-04-scroll-scatter.png` });

    // Scroll back to top and check narrow viewport
    for (let k = 0; k < 8; k++) {
      await page.mouse.wheel(0, -350);
      await page.waitForTimeout(70);
    }
    await page.waitForTimeout(900);
    await page.setViewportSize({ width: 820, height: 900 });
    await page.waitForTimeout(600);
    await page.screenshot({ path: `${artifacts}/form-a-05-narrow.png` });

    const state = await page.evaluate(() => {
      const h = window.heroForTest;
      return {
        quadCount: h._quadCards?.length || 0,
        hasParticles: Boolean(h._particleField),
        particleCount: h._particleField?.geometry?.attributes?.position?.count || 0,
        hasBackdrop: Boolean(h._auroraBackdrop),
        hasHtmlHud: Boolean(document.getElementById('aurora-wheel-hud'))
      };
    });

    console.log(JSON.stringify({ state, errors }, null, 2));
    assert.deepEqual(errors, []);
    assert.equal(state.quadCount, 4);
    assert.equal(state.hasParticles, true);
    assert.equal(state.hasHtmlHud, false);
  } finally {
    await browser.close();
  }
})().catch(e => {
  console.error(e);
  process.exitCode = 1;
});
