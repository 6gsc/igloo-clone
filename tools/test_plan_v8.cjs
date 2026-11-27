const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const pw = require(process.env.PLAYWRIGHT_ROOT || `${process.env.HOME}/.npm/_npx/f0a362733743bae2/node_modules/playwright`);
const url = process.argv[2] || 'http://127.0.0.1:8791/';
const artifacts = process.argv[3] || path.join(__dirname, '..', 'shots');

(async () => {
  fs.mkdirSync(artifacts, { recursive: true });
  const browser = await pw.chromium.launch();
  try {
    const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
    const errors = [];
    page.on('pageerror', e => errors.push(`PAGEERROR: ${e.message}`));
    page.on('console', m => {
      if (m.type() === 'error' || m.text().includes('not present in the MSDF')) {
        errors.push(`CONSOLE: ${m.text()}`);
      }
    });

    await page.route('**/App3D-aurora-preview-v8.js', async r => {
      const response = await r.fetch();
      const source = await response.text();
      const pat1 = /async init\(\)\{const e=await zt\.batched\("aurora-monolith-v5\.drc"\)/;
      const pat2 = /class jF\{constructor\(e\)\{/;
      assert.match(source, pat1);
      assert.match(source, pat2);
      const patched = source
        .replace(pat1, m => m.replace('const e=', 'window.heroForTest=this;const e='))
        .replace(pat2, m => m + 'window.__mainCtrl=this;');
      return r.fulfill({ response, body: patched });
    });

    await page.goto(url, { waitUntil: 'networkidle' });
    await page.mouse.move(10, 880);
    await page.waitForFunction(() => window.heroForTest?.scene.introTL?.progress() === 1, {}, { timeout: 45000 });
    await page.waitForTimeout(1600);

    // 1. Hero
    await page.screenshot({ path: `${artifacts}/v8-01-hero.png` });

    const jumpToSceneProgress = async (sceneIdx, prog, settleMs = 1200) => {
      await page.evaluate(({ sIdx, p }) => {
        const ctrl = window.__mainCtrl;
        let topY = 0;
        for (let k = 0; k < sIdx; k++) topY += ctrl.scrollComposers[k].passes[0].scene.height;
        const sc = ctrl.scrollComposers[sIdx].passes[0].scene;
        const targetY = topY - 1 + p * (sc.height + 1);
        ctrl.stopAutoCenter();
        ctrl.autoCenter.needed = false;
        ctrl.scroll.y = targetY;
        ctrl.scroll.targetY1 = targetY;
        ctrl.scroll.targetY2 = targetY;
        ctrl.autoCenter.lastTarget = targetY;
      }, { sIdx: sceneIdx, p: prog });
      await page.waitForTimeout(settleMs);
    };

    // 2. Internship 1: NIO (scene 1, progress 1/3)
    await jumpToSceneProgress(1, 1 / 3);
    await page.screenshot({ path: `${artifacts}/v8-02-intern1-nio.png` });

    // 3. Internship 2: Inovance (scene 1, progress 2/3)
    await jumpToSceneProgress(1, 2 / 3);
    await page.screenshot({ path: `${artifacts}/v8-03-intern2-inovance.png` });

    // 4. Shattered Stone Ring Fly-Through + Chapter Title (scene 2, progress 0.19)
    await jumpToSceneProgress(2, 0.19, 1300);
    await page.screenshot({ path: `${artifacts}/v8-04-rings-chapter.png` });

    // 5. Passing through the 2 stone rings (scene 2, progress 0.31)
    await jumpToSceneProgress(2, 0.31, 1200);
    await page.screenshot({ path: `${artifacts}/v8-05-rings-pass.png` });

    // 6. Project 1: BettaFish 100K Particle Astrolabe Sculpture (scene 2, progress 0.50)
    await jumpToSceneProgress(2, 0.50, 1800);
    await page.screenshot({ path: `${artifacts}/v8-06-project1-bettafish.png` });

    // 7. Fluid mouse ripple on Project 1 sculpture
    await page.mouse.move(660, 460, { steps: 8 });
    await page.mouse.move(780, 420, { steps: 10 });
    await page.waitForTimeout(350);
    await page.screenshot({ path: `${artifacts}/v8-07-project1-fluid-hover.png` });

    // 8. Project 2: Scroll-morphed 100K Particle 3-Tier Monolith (scene 2, progress 0.78)
    await page.mouse.move(20, 880);
    await jumpToSceneProgress(2, 0.78, 2200);
    await page.screenshot({ path: `${artifacts}/v8-08-project2-workflow.png` });

    // 9. Click Project 1 sculpture to enter Detail Room
    await jumpToSceneProgress(2, 0.50, 1400);
    await page.mouse.click(720, 450);
    await page.waitForTimeout(2600);
    const isDetailOpenAfterClick = await page.evaluate(() => ({
      open: window.__mainCtrl.isDetailOpen,
      idx: window.__mainCtrl.detailIndex
    }));
    await page.screenshot({ path: `${artifacts}/v8-09-project1-detail.png` });

    // Close detail room back to projects
    await page.evaluate(() => { window.__mainCtrl.navigateToSection('home', '/'); });
    await page.waitForFunction(() => window.__mainCtrl.isDetailOpen === false, {}, { timeout: 10000 });
    await page.waitForTimeout(700);

    // 10. Bottom entry pedestal (scene 3, progress 0.76)
    await jumpToSceneProgress(3, 0.76, 1500);
    await page.screenshot({ path: `${artifacts}/v8-10-bottom-links.png` });

    // 11. Click Project 2 sculpture (scene 2, progress 0.78) to verify AI Workflow detail room
    await jumpToSceneProgress(2, 0.78, 1800);
    await page.mouse.click(720, 450);
    await page.waitForTimeout(2600);
    await page.screenshot({ path: `${artifacts}/v8-13-project2-workflow-detail.png` });
    await page.evaluate(() => { window.__mainCtrl.navigateToSection('home', '/'); });
    await page.waitForFunction(() => window.__mainCtrl.isDetailOpen === false, {}, { timeout: 10000 });
    await page.waitForTimeout(700);

    // 12. Click Hero Quadrant [02] Inovance (top-right) to verify Inovance detail room
    await page.evaluate(() => {
      const ctrl = window.__mainCtrl;
      ctrl.stopAutoCenter();
      ctrl.scroll.y = 0;
      ctrl.scroll.targetY1 = 0;
      ctrl.scroll.targetY2 = 0;
      ctrl.autoCenter.lastTarget = 0;
    });
    await page.waitForTimeout(900);
    await page.evaluate(() => { window.heroForTest._lockHover = 1; });
    await page.waitForTimeout(200);
    await page.mouse.click(980, 360);
    await page.waitForTimeout(2600);
    await page.screenshot({ path: `${artifacts}/v8-12-intern2-inovance-detail.png` });
    await page.evaluate(() => { window.__mainCtrl.navigateToSection('home', '/'); });
    await page.waitForFunction(() => window.__mainCtrl.isDetailOpen === false, {}, { timeout: 10000 });
    await page.waitForTimeout(700);

    // 13. Test clicking Hero Quadrant [01] NIO directly (top-left)
    await page.evaluate(() => {
      const ctrl = window.__mainCtrl;
      ctrl.stopAutoCenter();
      ctrl.scroll.y = 0;
      ctrl.scroll.targetY1 = 0;
      ctrl.scroll.targetY2 = 0;
      ctrl.autoCenter.lastTarget = 0;
    });
    await page.waitForTimeout(900);
    await page.evaluate(() => { window.heroForTest._lockHover = 0; });
    await page.waitForTimeout(200);
    await page.mouse.click(460, 360);
    await page.waitForTimeout(2600);
    await page.screenshot({ path: `${artifacts}/v8-11-intern1-nio-detail.png` });
    const finalState = await page.evaluate(() => ({
      sceneCount: window.__mainCtrl.scrollComposers.length,
      internCubeCount: window.__mainCtrl.scrollComposers[1].passes[0].scene.cubes.length,
      projectItemCount: window.__mainCtrl.scrollComposers[2].passes[0].scene.items.length,
      heroClickDetailOpen: window.__mainCtrl.isDetailOpen,
      heroClickDetailIndex: window.__mainCtrl.detailIndex
    }));

    console.log(JSON.stringify({ isDetailOpenAfterClick, finalState, errors }, null, 2));
    assert.deepEqual(errors, []);
    assert.equal(isDetailOpenAfterClick.open, true);
    assert.equal(isDetailOpenAfterClick.idx, 2);
    assert.equal(finalState.sceneCount, 4);
    assert.equal(finalState.internCubeCount, 2);
    assert.equal(finalState.projectItemCount, 2);
    assert.equal(finalState.heroClickDetailOpen, true);
    assert.equal(finalState.heroClickDetailIndex, 0);
  } finally {
    await browser.close();
  }
})().catch(e => {
  console.error(e);
  process.exitCode = 1;
});
