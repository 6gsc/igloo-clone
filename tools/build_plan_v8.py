#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Plan v8 — 100% igloo-native Aesthetic Redo:
  Scene 0 (igloo):    Snow mountain Hero Form A (4 clickable quadrants, no Ctrip)
  Scene 1 (cubes):    Original 2 frozen internship ice cubes (NIO + Inovance)
  Scene 2 (projects): Native Shattered-Ring Fly-Through -> 100K Real-Time Fluid Particle
                      VDB Sculpture Gallery (BettaFish Multi-Agent + AI Workflow / KB)
  Scene 3 (entry):    Original bottom particle contact pedestal (Resume / Mail / Phone-WeChat)

Zero primitive Box/Sphere/Icosahedron geometries. Zero neon colors. 100% arctic silver-gray
monochrome world, built-in MSDF typography, and real GPU fluid VDB particle morphing.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NEW_CUBES_CONFIG = r'''cubes:[{title:"INTERN_01 · 蔚来 NIO\n用户生命周期 & 商业化转化",hash:"nio",date:"2026.04 - 2026.09",temp:-4,kind:"ice",obj:"cube1",innerobject:"nio_logo",interior:{enabled:!0,title:"////// 实习经历 01 · 蔚来 NIO（2026.04 - 2026.09）",subtitle:"产品运营实习生 · 用户生命周期与商业化转化",highlight:"★ 核心战绩：月留存 46% → 55.38% ｜ 新客转化 4% → 7% ｜ 日均 50+ 痛点",sections:[{heading:"[01] 生命周期预警与分层续费",body:"接手 250 人月度盘，用飞书多维表格搭建意愿追踪看板；\n针对原策略粗放问题，改用「60-40-20 天及临期」分级触达，\n推动月度留存率从 46% 升至 55.38%。"},{heading:"[02] 新客线索承接与产品转化",body:"跟进月均 200+ 新客线索，按画像拆成「新客体验激励 + 老客增值匹配」双路径，\n结合“无忧包”卖点与终端场景，将新客转化率从 4% 提至 7%。"},{heading:"[03] B2B2C 需求转译与协同交付",body:"依托 NUS 日均拆解 50+ 终端痛点，把 C 端模糊反馈转成 B 端标准交付单，\n联动外部生态品牌跑通「收集—协同—交付—回访」全链路。"}],content:`产品运营实习生 · 用户生命周期与商业化转化`,socialTitle:"/// 了解更多",social:[{name:"GH",link:"https://github.com/guishaocong"}],linkTitle:"/// 完整简历",links:[{name:"PDF 后续开放",link:""}],obj:"nio_logo",objScale:1.2}},{title:"INTERN_02 · 汇川技术\n研发协同流程 & 质量平台运营",hash:"inovance",date:"2026.10 - 至今",temp:-2,kind:"ice",obj:"cube3",innerobject:"inovance_logo",interior:{enabled:!0,title:"////// 实习经历 02 · 汇川技术（2026.10 - 至今）",subtitle:"产品运营 & 研发协同推进 · 从一线卡点到全链路提效",highlight:"★ 核心战绩：一次完成率 69% → 88% ｜ 周期减半 ｜ 补件 -51.8%",sections:[{heading:"[01] 10 类研发协同卡点重构",body:"深入一线梳理 10 类高频协同堵点，拉齐需求流转、跨团队交付与验收口径，\n推动一次完成率从 69% 升至 88%，整体办理周期缩短一半。"},{heading:"[02] 质量平台前置校验治理",body:"面向 8000+ 开发者排查提单回退原因，\n补齐字段规范与前置校验规则，补件率下降 51.8%。"},{heading:"[03] 协同工作台与问题库沉淀",body:"围绕业务侧 Bug 收集、转译、分级与验收，推动工作台迭代至 Task 57，\n沉淀 873 条问题库交接包并完成 77 条遗留问题核验。"}],content:`产品运营 & 研发协同流程推进 · 从一线卡点到全链路提效`,socialTitle:"/// 了解更多",social:[{name:"GH",link:"https://github.com/guishaocong"}],linkTitle:"/// 完整简历",links:[{name:"PDF 后续开放",link:""}],obj:"inovance_logo",objScale:1.1}},{title:"PROJECT_01 · 微舆 MULTI-AGENT",hash:"bettafish",date:"04/01/2025",temp:4,kind:"project",projectSlot:0,vdb:"project_bettafish_64",vdbScale:1.06,role:"AI 产品经理 · 3 类舆情场景 0→1 定义",metric:"★ 4 层拆解 · 9 类标签 18 字段 · 5 维 Eval 验收集",obj:"cube1",innerobject:"nio_logo",interior:{enabled:!0,title:"////// 项目经历 01 · 微舆（BettaFish）多 Agent 舆情系统（2025.04 - 2025.12）",subtitle:"AI 产品经理 · 从 0→1 方案定义与 Eval 评测闭环",highlight:"★ 核心战绩：24 条用例 5 维评测 ｜ 报告重复降 22% ｜ 完整度升 18%",sections:[{heading:"[01] 场景颗粒度诊断",body:"复盘品牌声誉、突发舆情与行业趋势 3 类场景，定位模型在行业术语、\n观点分层与策略可执行性上的不足，拆成「语料、画像、场景、指标」4 层架构。"},{heading:"[02] 语料规范与协同验证",body:"梳理 9 类语料标签与 18 个核心字段，产出分析框架与验收清单，\n配合研发完成 ForumEngine 场景化联调。"},{heading:"[03] 多 Agent 评测与坏例收敛",body:"搭建 24 条核心验收集，按角色互补、事实一致、冲突识别、引导有效、结论收敛 5 维\n记录 11 个 Bad Case，迭代后重复占比降 22%、完整度升 18%。"}],content:`AI 产品经理（2025.04 - 2025.12）· 从 0→1 方案定义与 Eval 评测闭环`,socialTitle:"/// 了解更多",social:[{name:"GH",link:"https://github.com/guishaocong"}],linkTitle:"/// 完整简历",links:[{name:"PDF 后续开放",link:""}],obj:"project_detail_1",objScale:1.65}},{title:"PROJECT_02 · AI 工作流与知识库",hash:"ai-workflow",date:"11/01/2026",temp:7,kind:"project",projectSlot:1,vdb:"project_workflow_64",vdbScale:1.12,role:"个人效率工程 · Dify / n8n / Claude Code",metric:"★ _kb + _meta + Skill 三层架构 · 全链路可回源",obj:"cube3",innerobject:"inovance_logo",interior:{enabled:!0,title:"////// 项目经历 02 · AI 工作流与可回源知识库（2026）",subtitle:"AI 工具链设计与工程提效实践 · Dify / n8n / Claude Code",highlight:"★ 核心战绩：三层可回源知识架构 ｜ 手工动作工具化 ｜ Dify / n8n 验证",sections:[{heading:"[01] 三层知识库与证据核查",body:"落地 _kb + _meta + Skill 三层架构，为每条产品文档与走查记录配原件编号、\n文件指纹校验和 [F/I/P/U] 口径分级，确保结论可回源核查。"},{heading:"[02] AI Coding 辅助交付流",body:"沉淀「读代码—理链路—拆需求—调脚本—做验证」交付流程，\n使用 Claude Code 与 Cursor 写出多端轨迹抓取脚本及本 3D 个人站点原型。"},{heading:"[03] 自动化业务工作流验证",body:"用 Dify 和 n8n 跑通知识检索、反馈归类与重复数据处理链路，\n将高频手工整理工作转化为可复用技能卡。"}],content:`AI 工作流设计与工程提效实践 · Dify / n8n / Claude Code / 可回源知识体系`,socialTitle:"/// 了解更多",social:[{name:"GH",link:"https://github.com/guishaocong"}],linkTitle:"/// 完整简历",links:[{name:"PDF 后续开放",link:""}],obj:"project_detail_2",objScale:1.65}}]'''

HERO_COPY_PATCHES = [
    (
        'manifesto:{title:"////// Profile",text:"习惯从一线业务卡点切入，\\n擅长用流程重构、数据漏斗\\n与评测体系驱动产品落地。"}',
        'manifesto:{title:"////// Profile",text:"专注产品运营与流程提效，\\n用数据漏斗拉升留存转化，\\n结合 AI 工作流加速落地。"}'
    ),
    (
        'scroll:"向下滚动 · 查看项目拆解与简历"',
        'scroll:"向下滚动 · 查看核心战绩与简历"'
    ),
    (
        'const hKicker = makeMsdfText("////// 3年产品实战 · 需求定义 → 指标闭环", 0.255, "#CBE0FF", 14.5, 0.042, 0.62);',
        'const hKicker = makeMsdfText("////// 3年实战 · 数据增长 × 协同提效 × AI 落地", 0.255, "#CBE0FF", 14.5, 0.042, 0.62);'
    ),
    (
        'const hTitle = makeMsdfText("AI 产品经理 · 产品运营", 0.70, Be.colorText, 14.5, 0.052, 0.65);',
        'const hTitle = makeMsdfText("产品运营 · AI 产品经理", 0.70, Be.colorText, 14.5, 0.052, 0.65);'
    ),
    (
        'const hSub = makeMsdfText("智能体系统设计  ·  用户增长运营  ·  自动化提效", 0.28, "#F2F7FF", 14.5, 0.044, 0.62);',
        'const hSub = makeMsdfText("用户增长漏斗  ·  研发协同提效  ·  AI 工作流与评测", 0.28, "#F2F7FF", 14.5, 0.044, 0.62);'
    ),
    (
        'this._activeTitle = "AI 产品经理 · 产品运营";',
        'this._activeTitle = "产品运营 · AI 产品经理";'
    ),
    (
        'const tagRow1 = makeMsdfText("[ Claude Code / Cursor ]  [ Dify / n8n ]  [ RAG / MCP / Function Calling ]", 0.25, Be.colorText, 17.5, 0.044, 0.65);',
        'const tagRow1 = makeMsdfText("[ SQL / Python Pandas ]  [ 飞书多维表格 / NUS ]  [ Axure / Figma ]", 0.25, Be.colorText, 17.5, 0.044, 0.65);'
    ),
    (
        'const tagRow2 = makeMsdfText("[ SQL / Python Pandas ]  [ Axure / Figma ]  [ 国一 · 软硬双高级认证 ]", 0.245, "#E8F2FF", 17.5, 0.042, 0.65);',
        'const tagRow2 = makeMsdfText("[ Dify / n8n / Claude Code ]  [ RAG / MCP ]  [ 国一 · 软硬双高级认证 ]", 0.245, "#E8F2FF", 17.5, 0.042, 0.65);'
    ),
]

HERO_QUAD_OLD = r'''    const QUAD_SPECS = [
        {
            id: 0,
            pos: [-2.98,  0.46,  0.14],
            anchor: [-0.48,  0.34, -0.05],
            kicker: "[ 01 ] 汇川 · 研发协同提效",
            metric: "69% → 88%",
            proof: "10类事项一次完成 · 周期减半",
            scatter: [-2.05, 0.90, 1.40]
        },
        {
            id: 1,
            pos: [ 2.98,  0.46, -0.06],
            anchor: [ 0.48,  0.34, -0.10],
            kicker: "[ 02 ] 蔚来 NIO · 生命周期",
            metric: "46% → 55.38%",
            proof: "250人盘月留存 · 转化 4%→7%",
            scatter: [ 2.05, 0.90, 1.30]
        },
        {
            id: 2,
            pos: [-2.98, -0.96, -0.06],
            anchor: [-0.48, -0.86, -0.10],
            kicker: "[ 03 ] 微舆 · Multi-Agent",
            metric: "-22% / +18%",
            proof: "24用例5维Eval · 重复降/完整升",
            scatter: [-2.05, -0.70, 1.30]
        },
        {
            id: 3,
            pos: [ 2.98, -0.96,  0.14],
            anchor: [ 0.48, -0.86, -0.05],
            kicker: "[ 04 ] 质量平台 & 携程洞察",
            metric: "8000+ 开发者",
            proof: "补件 -51.8% · 携程负反馈 -32%",
            scatter: [ 2.05, -0.70, 1.45]
        }
    ];'''

HERO_QUAD_NEW = r'''    const QUAD_SPECS = [
        {
            id: 0,
            pos: [-2.98,  0.46,  0.14],
            anchor: [-0.48,  0.34, -0.05],
            kicker: "[ 01 ] 蔚来 NIO · 用户留存",
            metric: "46% → 55.38%",
            proof: "250人月度盘 · 新客转化 4%→7%",
            scatter: [-2.05, 0.90, 1.40]
        },
        {
            id: 1,
            pos: [ 2.98,  0.46, -0.06],
            anchor: [ 0.48,  0.34, -0.10],
            kicker: "[ 02 ] 汇川 · 研发协同提效",
            metric: "69% → 88%",
            proof: "10类事项一次完成 · 周期减半",
            scatter: [ 2.05, 0.90, 1.30]
        },
        {
            id: 2,
            pos: [-2.98, -0.96, -0.06],
            anchor: [-0.48, -0.86, -0.10],
            kicker: "[ 03 ] 汇川 · 质量平台治理",
            metric: "补件 -51.8%",
            proof: "覆盖 8000+ 开发者 · 校验前置",
            scatter: [-2.05, -0.70, 1.30]
        },
        {
            id: 3,
            pos: [ 2.98, -0.96,  0.14],
            anchor: [ 0.48, -0.86, -0.05],
            kicker: "[ 04 ] 微舆 · Multi-Agent",
            metric: "-22% / +18%",
            proof: "24用例5维Eval · 重复降/完整升",
            scatter: [ 2.05, -0.70, 1.45]
        }
    ];'''

HERO_CLICK_OLD = r'''    this._t0 = performance.now() * 0.001;
    this._localMouse = new b(99, 99, 0);
}'''

HERO_CLICK_NEW = r'''    this._t0 = performance.now() * 0.001;
    this._localMouse = new b(99, 99, 0);

    const QUAD_HASHES = ["nio", "inovance", "inovance", "bettafish"];
    if (!this._heroClickBound) {
        this._heroClickBound = !0;
        let downX = 0, downY = 0;
        window.addEventListener("pointerdown", (ev) => {
            downX = ev.clientX;
            downY = ev.clientY;
        }, { passive: !0 });
        window.addEventListener("pointerup", (ev) => {
            const sc = this.scene;
            if (!sc || !sc.isSceneVisible) return;
            if (sc.controller && (sc.controller.isDetailOpen || sc.controller.scrollBlocked)) return;
            if (Math.hypot(ev.clientX - downX, ev.clientY - downY) > 6) return;
            if (!this._auroraRoot || !this._auroraRoot.visible) return;
            if (this._particleField && this._particleField.material.uniforms.uScatter.value > 0.12) return;
            const qIdx = this._hoveredQuad;
            if (qIdx >= 0 && qIdx < QUAD_HASHES.length) {
                Q.emit("webgl_switch_scene", `portfolio/${QUAD_HASHES[qIdx]}`);
            }
        });
    }
}'''

PLAN8_PROJECT_SCENE = r'''
class Plan8ProjectParticles {
    constructor(scene, items) {
        this.scene = scene;
        this.items = items;
        this.ready = new Promise(t => { this.isReady = t; });
        this.cubeSize = 0.72;
        this.particles = 150 * 1e3;
        this.fluidSim = new $U({
            borders: !1,
            simRes: 128,
            dyeRes: 128,
            curlStrength: 0,
            splatRadius: 0.22,
            splatForce: 34,
            pressureIterations: 2,
            densityDissipation: 0.88,
            velocityDissipation: 0.98,
            pressureDissipation: 0.86,
            splatRadiusVelocity: !1,
            renderEvent: !1
        });
        this.fluidSim.disable();
        this.currentIdx = 0;
        this.vdbs = [];
        this.vdbScales = items.map(it => it.vdbScale || 1.18);
        this.init();
    }
    async init() {
        const first = await le.load(`volumes/${this.items[0].vdb}.ktx2`, "3d-data");
        this.vdbs.push(first);
        for (let i = 1; i < this.items.length; i++) {
            this.vdbs.push(le.load(`volumes/${this.items[i].vdb}.ktx2`, "3d-data"));
        }
        const texSize = ie.getTextureSizeParticles(this.particles);
        const initPos = new Float32Array(texSize * texSize * 4);
        for (let i = 0; i < this.particles; i++) {
            initPos[i * 4 + 0] = ie.fit(Math.random(), 0, 1, -this.cubeSize * 0.5, this.cubeSize * 0.5);
            initPos[i * 4 + 1] = ie.fit(Math.random(), 0, 1, -this.cubeSize * 0.5, this.cubeSize * 0.5);
            initPos[i * 4 + 2] = ie.fit(Math.random(), 0, 1, -this.cubeSize * 0.5, this.cubeSize * 0.5);
            initPos[i * 4 + 3] = Math.random();
        }
        const tPos = new Hi(initPos, texSize, texSize, wt, Lt);
        tPos.needsUpdate = !0;
        const tVel = new Hi(new Float32Array(texSize * texSize * 4), texSize, texSize, wt, Lt);
        tVel.needsUpdate = !0;
        const tOrig = new Hi(initPos.slice(), texSize, texSize, wt, Lt);
        tOrig.needsUpdate = !0;
        const lightPos = new b(-0.52, 0.85, 0.92);

        this.mesh = new gE({
            count: this.particles,
            geometry: "points",
            material: new fe({
                uniformsGroups: [he.UBO],
                uniforms: {
                    tTexture1: { value: null },
                    tTexture2: { value: null },
                    uColorInitial: { value: new Z("#c8d6ea") },
                    uColorLight: { value: new Z("#d2dbe8") },
                    uColorDark: { value: new Z("#313c52") },
                    uColorFast: { value: new Z("#ecf4ff") },
                    uSize: { value: 9.0 },
                    uLightPos: { value: lightPos },
                    uVisible: { value: 0 },
                    uAlpha: { value: 1 },
                    uInitialGlow: { value: 0 }
                },
                vertexShader: `
                    ${ae}
                    attribute vec4 rand;
                    attribute vec2 texuv;
                    uniform sampler2D tTexture1;
                    uniform sampler2D tTexture2;
                    uniform float uSize;
                    varying float vShadow;
                    varying float vVel;
                    void main() {
                        vec4 posData = texture2D(tTexture1, texuv);
                        vec4 velData = texture2D(tTexture2, texuv);
                        vec3 pos = posData.xyz;
                        vec4 vPos = modelViewMatrix * vec4(pos, 1.0);
                        vShadow = posData.w;
                        vVel = velData.w;
                        gl_Position = projectionMatrix * vPos;
                        gl_PointSize = uSize / max(length(vPos.xyz), 0.45) * (resolution.y / 1300.0);
                    }
                `,
                fragmentShader: `
                    ${ae}
                    ${Zo}
                    ${Ht}
                    ${yd}
                    ${AF}
                    uniform vec3 uColorLight;
                    uniform vec3 uColorDark;
                    uniform vec3 uColorInitial;
                    uniform vec3 uColorFast;
                    uniform vec3 uLightPos;
                    uniform float uVisible;
                    uniform float uAlpha;
                    uniform float uInitialGlow;
                    varying float vShadow;
                    varying float vVel;
                    void main() {
                        float alpha = step(length(gl_PointCoord.xy - 0.5), 0.5) * uVisible;
                        if (alpha < 0.001) discard;
                        vec2 uv = 2.0 * gl_PointCoord.xy - 1.0;
                        vec3 n = vec3(uv, sqrt(1.0 - clamp(dot(uv, uv), 0.0, 1.0)));
                        n.y = 1.0 - n.y;
                        // Front-lit studio key light with rich sculptural midtone relief
                        float lightShadow = max(0.0, dot(normalize(uLightPos), normalize(n)));
                        float ramp = mix(0.22, 1.0, lightShadow) * vShadow;
                        vec3 color = mix(uColorDark, uColorLight, clamp(ramp, 0.0, 1.0));
                        color = mix(color, uColorFast, pow(fit(vVel, 0.003, 0.005, 0.0, 1.0), 2.0));
                        alpha *= max(uInitialGlow, pow(fit(vVel, 0.002, 0.007, 1.0, 0.0), 2.0) * 0.5 + 0.5);
                        vec3 fadeInColor = mix(vec3(1.0), uColorInitial, linearstep(0.0, 1.0, uAlpha));
                        color = mix(color, fadeInColor, uInitialGlow);
                        gl_FragColor = vec4(clamp(color, 0.0, 1.0), alpha * uAlpha);
                    }
                `,
                depthTest: !0,
                depthWrite: !0,
                transparent: !0,
                blending: cy,
                blendEquation: ar,
                blendDst: hy,
                blendSrc: Ou
            })
        }, {
            textures: 2,
            initialTextures: [tPos, tVel],
            material: new fe({
                uniformsGroups: [he.UBO],
                uniforms: {
                    tTexture1: { value: null },
                    tTexture2: { value: null },
                    tOrig: { value: tOrig },
                    tVel: this.fluidSim.velUniform,
                    uViewMatrix: { value: new De },
                    uModelMatrix: { value: new De },
                    uProjMatrix: { value: new De },
                    uRotation: { value: 0.25 },
                    uCubeSize: { value: this.cubeSize },
                    tVolume: { value: this.vdbs[0] },
                    uVolumeScale: { value: this.vdbScales[0] },
                    uLightPos: { value: lightPos },
                    uInteractForce: { value: 1 },
                    uAdditionalNoise: { value: 0 },
                    uShowNoise: { value: 0 }
                },
                vertexShader: `
                    attribute vec4 rand;
                    varying vec4 vRand;
                    void main() {
                        vRand = rand;
                        gl_Position = vec4(position, 1.0);
                    }
                `,
                fragmentShader: `
                    varying vec4 vRand;
                    #define outPos pc_fragColor
                    uniform sampler2D tTexture1;
                    layout(location = 1) out highp vec4 outVel;
                    uniform sampler2D tTexture2;
                    uniform sampler2D tOrig;
                    uniform sampler2D tVel;
                    uniform mat4 uProjMatrix;
                    uniform mat4 uViewMatrix;
                    uniform mat4 uModelMatrix;
                    uniform float uCubeSize;
                    uniform vec3 uLightPos;
                    uniform float uRotation;
                    uniform float uAdditionalNoise;
                    uniform float uShowNoise;
                    uniform float uInteractForce;
                    #ifdef GL_FRAGMENT_PRECISION_HIGH
                        precision highp sampler3D;
                    #else
                        precision mediump sampler3D;
                    #endif
                    uniform sampler3D tVolume;
                    uniform float uVolumeScale;
                    ${ae}
                    ${pF}
                    ${mF}
                    ${yd}
                    void main() {
                        ivec2 uv = ivec2(gl_FragCoord.xy);
                        vec4 currentPos = texelFetch(tTexture1, uv, 0);
                        vec4 currentVel = texelFetch(tTexture2, uv, 0);

                        mat3 rotMatrix = rotateY(uRotation);
                        vec3 samplePos = rotMatrix * (currentPos.xyz / uCubeSize) * uVolumeScale + 0.5;
                        vec4 volData = texture(tVolume, samplePos);
                        vec3 grad = normalize(volData.rgb * 2.0 - 1.0) * rotMatrix;
                        float dist = (volData.a * 2.0 - 1.0) * 2.0;

                        float pushForce = 0.00055;
                        vec4 wPos = uModelMatrix * vec4(currentPos.xyz, 1.0);
                        vec4 vPos = uViewMatrix * wPos;
                        vec4 posProjected = uProjMatrix * vPos;
                        vec2 uvScreen = (posProjected.xy / posProjected.w + 1.0) * 0.5;
                        vec3 vel = texture2D(tVel, uvScreen).xyz;
                        vec3 up = vec3(uViewMatrix[0][1], uViewMatrix[1][1], uViewMatrix[2][1]);
                        vec3 right = vec3(uViewMatrix[0][0], uViewMatrix[1][0], uViewMatrix[2][0]);
                        vec3 disp = right * vel.x + up * vel.y;
                        currentVel.xyz += disp * pushForce * dtRatio * uInteractForce;
                        float invFluidStrength = 1.0 - length(vel) * 0.65 * uInteractForce;

                        float additionalNoise = max(uAdditionalNoise, uShowNoise);
                        float force1 = 0.00018 * (0.7 + 0.3 * vRand.z) + 0.00048 * additionalNoise;
                        currentVel.xyz += BitangentNoise4D(vec4((currentPos.xyz) * 7.0, time * (1.0 + 0.7 * vRand.y))) * force1 * dtRatio;

                        vec4 origPos = texelFetch(tOrig, uv, 0);
                        currentVel.xyz += (origPos.xyz - currentPos.xyz) * 0.001 * dtRatio * invFluidStrength;

                        float force2 = 0.0016 * (0.7 + 0.3 * vRand.w);
                        float signForce = mix(0.0, -0.32, sign(dist) + 1.0);
                        currentVel.xyz += grad * force2 * signForce * dtRatio * invFluidStrength;

                        currentVel.xyz *= frictionFPS(0.9, dtRatio);
                        currentPos.xyz += currentVel.xyz * dtRatio;

                        currentPos.y = clamp(currentPos.y, -0.37, 0.37);
                        currentPos.xz = normalize(currentPos.xz + vec2(1e-5)) * clamp(length(currentPos.xz), 0.0, 0.36);

                        vec3 lightPos = normalize(uLightPos);
                        float wrap = 0.42;
                        float dp = dot(lightPos, grad);
                        float wrapDiffuse = max(0.0, (dp + wrap) / (1.0 + wrap));
                        wrapDiffuse += max(0.0, -dp) * 0.16;
                        float targetShadow = mix(wrapDiffuse * 0.42, wrapDiffuse, smoothstep(-0.05, -0.001, dist));
                        currentPos.a = mix(targetShadow, currentPos.a, additionalNoise);
                        currentVel.a = lerpFPS(currentVel.a, length(currentVel.xyz), 0.035, dtRatio);

                        outVel = currentVel;
                        outPos = currentPos;
                    }
                `
            })
        });
        this.mesh.name = "project_volume_particles";
        this.mesh.position.set(0, 0, -0.55);
        this.mesh.renderOrder = 12;
        this.mesh.updateMatrixWorld();
        this.scene.add(this.mesh);

        // Pre-warm particles so sculpture is crisp from frame 1
        let warmup = 0;
        const stepWarm = () => {
            warmup += Fe.delta;
            this.mesh.compute(void 0, this.scene, this.scene.camera);
            if (warmup > 900) {
                Q.off("webgl_prerender", stepWarm);
                this.mesh.material.uniforms.uVisible.value = 1;
            }
        };
        Q.on("webgl_prerender", stepWarm);
        this.isReady();
    }
    setProjectIndex(idx, instant = !1) {
        const clamped = ie.clamp(idx, 0, this.items.length - 1);
        if (clamped === this.currentIdx && !instant) return;
        this.currentIdx = clamped;
        const u = this.mesh.computationMaterial.uniforms;
        u.tVolume.value = this.vdbs[clamped];
        u.uVolumeScale.value = this.vdbScales[clamped];
        if (!instant) {
            re.fromTo(u.uAdditionalNoise, { value: 1.0 }, { value: 0.0, duration: 0.72, ease: "power2.inOut", overwrite: !0 });
            Q.emit("webgl_play_audio", "ui-long");
        }
    }
    update(interactStrength, alphaVal, showNoiseVal) {
        if (this.scene.isSceneVisible) {
            this.fluidSim.enable();
            this.fluidSim.points[0].position.copy($t.get(0).position01);
            this.fluidSim._update(Fe.time, Fe.delta);
        } else {
            this.fluidSim.disable();
        }
        const u = this.mesh.computationMaterial.uniforms;
        // Graceful sculptural sway (±26 deg facing the viewer so BettaFish & ✦ AI Sparkle stay iconic)
        u.uRotation.value = Math.sin(Fe.time * 0.42) * 0.44;
        u.uInteractForce.value = interactStrength;
        u.uShowNoise.value = showNoiseVal;
        this.mesh.material.uniforms.uAlpha.value = alphaVal;
        this.mesh.material.uniforms.uInitialGlow.value = showNoiseVal * 0.55;
    }
}

class Plan8ProjectScene extends Jo {
    constructor(e = {}) {
        super({ orbit: !1 });
        this.controller = e.mainController;
        this.items = Be.cubes.filter(c => c.kind === "project");
        this.progress = 0;
        this.height = 4.2;
        this.initialScrollAutocenter = 0.22;
        this.finalScrollAutocenter = 0.80;
        this._isSceneVisible = !1;
        this.cameraZoom = { value: 0 };
        this.rings = [];
        this.activeIdx = 0;
        this._hudAlpha = 0;
        this._hudDecode = { value: 1 };
        this._hudTextMeshes = [];
        this._chapterMeshes = [];
        this._clickBound = !1;
        this.init();
    }
    get isSceneVisible() { return this._isSceneVisible; }
    set isSceneVisible(e) {
        const changed = this._isSceneVisible !== e;
        this._isSceneVisible = e;
        if (changed && !e && this.particles) {
            this.particles.fluidSim.disable();
        }
    }
    async init() {
        this.cameraOptions();
        this.renderOptions();
        await Promise.all([
            this.createBg(),
            this.createBlurryText(),
            this.createBackgroundShapes(),
            this.createTransitionRings(),
            this.createParticles(),
            this.createTypography()
        ]);
        this.bindInteraction();
        this.resize();
        Q.on("resize", this.resize, this);
        this.beforeRenderCbs.push(this.update.bind(this));
        this.isReady();
    }
    cameraOptions() {
        this.camera.fov = 28;
        this.camera.updateProjectionMatrix();
        this.camera.basePosition.set(0, 0, 5.2);
        this.camera.baseTarget.set(0, 0, -0.55);
        this.camera.displacement.position.set(0.05, 0.025);
        this.camera.lerpPosition = 0.08;
        this.camera.lerpTarget = 0.08;
        this.camera.shake.setScalar(0.012);
        this.camera.shakeSpeed.setScalar(0.18);
    }
    renderOptions() {
        Promise.resolve().then(() => {
            O3(this, this.composer);
            const e = q.devScene ? this.composer : he.composer;
            e.__hasBloomPass || (e.__hasBloomPass = !0, e.addPass(new Fd().addBloom({ debug: q.devScene, levels: 6, luminanceThreshold: 0.2, intensity: 1, radius: 0.85 })));
        });
    }
    async createBg() { this.bg = new k3(this); await this.bg.ready; }
    async createBlurryText() { this.blurrytext = new z3(this); await this.blurrytext.ready; }
    async createBackgroundShapes() { this.backgroundshapes = new rF(this); await this.backgroundshapes.ready; }
    async createTransitionRings() {
        const specs = [
            { name: "shattered_ring2", z: 2.75, scale: 2.45, rotZ: 0.15 },
            { name: "shattered_ring",  z: 1.25, scale: 2.05, rotZ: -0.45 }
        ];
        const geoms = await Promise.all(specs.map(s => zt.load(`${s.name}.drc`)));
        specs.forEach((sp, i) => {
            const mat = new lF();
            mat.uniforms.tMap.value = le.load(`${sp.name}_color.ktx2`, "srgb-repeat");
            mat.uniforms.tGlow.value = le.load(`${sp.name}_ao.ktx2`, "srgb-repeat");
            const mesh = new Ce(geoms[i], mat);
            mesh.name = `project_ring_${i}`;
            // shattered_ring.drc natively lies in XY plane (radius ~0.40) facing +Z
            mesh.rotation.set(0, 0, sp.rotZ);
            mesh.position.set(0, 0, sp.z);
            mesh.scale.setScalar(sp.scale);
            mesh.renderOrder = 6 + i;
            mesh.frustumCulled = !1;
            this.add(mesh);
            this.rings.push({ mesh, baseZ: sp.z, baseRotZ: sp.rotZ, speed: i === 0 ? 0.10 : -0.14 });
        });
    }
    async createParticles() {
        this.particles = new Plan8ProjectParticles(this, this.items);
        await this.particles.ready;
    }
    async createTypography() {
        const tFontMap = le.load("../fonts/IBMPlexMono-Medium-datatexture.ktx2", "data");
        const makeMsdf = (str, size, hex, align = "center", width = 4.0, weight = 0.038, halo = 0.42) => {
            const m = new Ui({
                font: "IBMPlexMono-Medium",
                text: str,
                width,
                align,
                lineHeight: 0.96,
                size
            }, {
                uniforms: {
                    tMap: { value: tFontMap },
                    uColor: { value: new Z(hex) },
                    uShow1: { value: 1.0 },
                    uShow2: { value: 1.0 },
                    uOpacity: { value: 0.0 },
                    uWeight: { value: weight },
                    uShadow: { value: halo }
                },
                vertexShader: `
                    ${Nt}
                    ${Ue}
                    attribute vec3 textWeights;
                    uniform float uShow1;
                    uniform float uShow2;
                    varying vec2 vUv;
                    varying float vAlpha;
                    void main() {
                        float tr1 = falloff(textWeights.x, 0.0, 1.0, 0.1, clamp(uShow1, 0.0, 1.0));
                        float tr2 = falloff(textWeights.x, 0.0, 1.0, 1.0, clamp(uShow2, 0.0, 1.0));
                        vUv = uv;
                        vUv.x = mod(uv.x + 0.125 * mod(floor((1.0 - tr2) * 5.753), 8.0), 1.0);
                        vAlpha = tr1;
                        gl_Position = projectionMatrix * viewMatrix * billboardModelMatrix() * vec4(position, 1.0);
                    }
                `,
                fragmentShader: `
                    ${ii}
                    ${Ht}
                    ${Ue}
                    uniform sampler2D tMap;
                    uniform vec3 uColor;
                    uniform float uOpacity;
                    uniform float uWeight;
                    uniform float uShadow;
                    varying vec2 vUv;
                    varying float vAlpha;
                    void main() {
                        float sd = median(tMap, vUv);
                        float d = max(fwidth(sd), 0.0001);
                        float fill = smoothstep(-d, d, sd + uWeight);
                        float back = smoothstep(-0.32, 0.02, sd + uWeight) * uShadow;
                        float outA = max(fill, back) * vAlpha * uOpacity;
                        if (outA < 0.01) discard;
                        vec3 shCol = vec3(0.18, 0.22, 0.29);
                        vec3 finalCol = mix(shCol, uColor, fill / max(max(fill, back), 0.001));
                        gl_FragColor = vec4(finalCol, outA);
                    }
                `,
                transparent: !0,
                depthWrite: !1,
                depthTest: !1
            });
            m.frustumCulled = !1;
            m.renderOrder = 30;
            return m;
        };

        // Chapter transition typography (pure frameless arctic typography dead-center inside Ring 1 aperture)
        this.chapterGroup = new Gi();
        this.chapterGroup.position.set(0, 0, 1.55);
        this.add(this.chapterGroup);
        const cKicker = makeMsdf("////// CHAPTER 02 · AI PROJECTS", 0.052, "#3C3C54", "center", 3.8, 0.036, 0.16);
        cKicker.position.set(0, 0.165, 0);
        const cTitle = makeMsdf("AI 系统设计与提效实战", 0.115, "#ffffff", "center", 4.5, 0.046, 0.45);
        cTitle.position.set(0, 0.015, 0);
        const cSub = makeMsdf("多智能体评测闭环 · 可回源知识工程", 0.046, "#eef4fc", "center", 4.5, 0.036, 0.36);
        cSub.position.set(0, -0.135, 0);
        this.chapterGroup.add(cKicker, cTitle, cSub);
        this._chapterMeshes = [cKicker, cTitle, cSub];

        // Per-project minimalist spatial HUD (matches cubes leader-line typography — zero boxes, safe margins!)
        this.hudGroup = new Gi();
        this.hudGroup.position.set(0, 0, -0.55);
        this.add(this.hudGroup);

        // Subtle thin architectural leader lines (safely below top-left Gui logo & inside ±0.64 viewport)
        const linePts = [
            -0.25,  0.15, 0.05,  -0.36,  0.24, 0.05,
            -0.36,  0.24, 0.05,  -0.63,  0.24, 0.05,
             0.25, -0.14, 0.05,   0.36, -0.22, 0.05,
             0.36, -0.22, 0.05,   0.63, -0.22, 0.05
        ];
        const lGeo = new ot();
        lGeo.setAttribute("position", new nt(linePts, 3));
        this._hudLineMat = new ga({ color: "#ffffff", opacity: 0, transparent: !0, depthTest: !1, depthWrite: !1, blending: pt });
        this._hudLines = new yr(lGeo, this._hudLineMat);
        this._hudLines.renderOrder = 25;
        this.hudGroup.add(this._hudLines);

        // Minimalist left/right chevron arrows (native igloo style, well inside ±0.66)
        const arrowPts = [
            -0.67,  0.00, 0.05,  -0.62,  0.036, 0.05,
            -0.67,  0.00, 0.05,  -0.62, -0.036, 0.05,
             0.67,  0.00, 0.05,   0.62,  0.036, 0.05,
             0.67,  0.00, 0.05,   0.62, -0.036, 0.05
        ];
        const aGeo = new ot();
        aGeo.setAttribute("position", new nt(arrowPts, 3));
        this._arrowMat = new ga({ color: "#ffffff", opacity: 0, transparent: !0, depthTest: !1, depthWrite: !1, blending: pt });
        this._arrows = new yr(aGeo, this._arrowMat);
        this._arrows.renderOrder = 26;
        this.hudGroup.add(this._arrows);

        this._projectHudSets = this.items.map((it, idx) => {
            const g = new Gi();
            g.visible = idx === 0;
            const tTitle = makeMsdf(it.title.toUpperCase(), 0.036, "#ffffff", "left", 1.15, 0.042, 0.36);
            tTitle.position.set(-0.50, 0.278, 0.05);

            const tMeta = makeMsdf(`D ${it.date.replaceAll("/", ".")}\nCLICK TO EXPLORE`, 0.030, "#ffffff", "right", 0.85, 0.038, 0.32);
            tMeta.position.set(0.515, -0.172, 0.05);

            const tRole = makeMsdf(`0${idx + 1} / 0${this.items.length}  ·  ${it.role}`, 0.030, "#3C3C54", "center", 2.4, 0.036, 0.14);
            tRole.position.set(0, -0.355, 0.05);

            const tMetric = makeMsdf(it.metric, 0.034, "#ffffff", "center", 2.7, 0.042, 0.42);
            tMetric.position.set(0, -0.415, 0.05);

            g.add(tTitle, tMeta, tRole, tMetric);
            this.hudGroup.add(g);
            return { group: g, meshes: [tTitle, tMeta, tRole, tMetric] };
        });

        const allReady = [
            ...this._chapterMeshes.map(m => m.ready),
            ...this._projectHudSets.flatMap(s => s.meshes.map(m => m.ready))
        ];
        await Promise.all(allReady);
    }
    bindInteraction() {
        if (this._clickBound) return;
        this._clickBound = !0;
        let dx = 0, dy = 0;
        window.addEventListener("pointerdown", (ev) => { dx = ev.clientX; dy = ev.clientY; }, { passive: !0 });
        window.addEventListener("pointerup", (ev) => {
            if (!this._isSceneVisible) return;
            if (this.controller && (this.controller.isDetailOpen || this.controller.scrollBlocked)) return;
            if (Math.hypot(ev.clientX - dx, ev.clientY - dy) > 8) return;
            if (this.progress < 0.32 || this.progress > 0.94) return;
            const nx = (ev.clientX / Math.max(window.innerWidth, 1)) * 2 - 1;
            const ny = (ev.clientY / Math.max(window.innerHeight, 1)) * 2 - 1;
            if (Math.abs(nx) < 0.34 && Math.abs(ny) < 0.56) {
                const it = this.items[this.activeIdx];
                if (it) Q.emit("webgl_switch_scene", `portfolio/${it.hash}`);
            } else if (Math.abs(ny) < 0.35 && Math.abs(nx) >= 0.34 && Math.abs(nx) < 0.78) {
                const next = nx > 0 ? (this.activeIdx + 1) % this.items.length : (this.activeIdx + this.items.length - 1) % this.items.length;
                this.jumpToProjectSlot(next);
            }
        });
    }
    jumpToProjectSlot(slotIdx) {
        const targetP = slotIdx === 0 ? 0.50 : 0.78;
        this.switchActiveProject(slotIdx);
        if (this.controller) {
            const curDelta = (targetP - this.progress) * (this.height + 1);
            this.controller.centerScroll(this.controller.scroll.y + curDelta, 1.1);
        }
    }
    switchActiveProject(idx, instant = !1) {
        const clamped = ie.clamp(idx, 0, this.items.length - 1);
        if (clamped === this.activeIdx && !instant) return;
        this.activeIdx = clamped;
        if (this.particles) this.particles.setProjectIndex(clamped, instant);
        this._projectHudSets.forEach((set, i) => {
            set.group.visible = i === clamped;
        });
        if (!instant) {
            re.fromTo(this._hudDecode, { value: 0 }, { value: 1, duration: 0.72, ease: "power2.out", overwrite: !0 });
        }
    }
    getStopProgressForSlot(slotIdx) {
        return slotIdx === 0 ? 0.50 : 0.78;
    }
    update() {
        const p = this.progress;
        // Phase 1 (0 -> 0.42): Seamless camera glide forward through both sculpted shattered stone rings
        const flyT = ie.smoothstep(0.06, 0.44, p);
        // Phase 2 (0.44 -> 0.86): Gentle orbital drift around sculpture as project 1 morphs into project 2
        const orbT = ie.smoothstep(0.46, 0.80, p);
        const camZ = ie.mix(5.20, 1.38, flyT) + Math.sin(orbT * Math.PI) * 0.18 + this.cameraZoom.value;
        const camX = -0.14 * Math.sin(flyT * Math.PI) + (orbT - 0.5) * 0.24;
        const camY = 0.08 * Math.sin(flyT * Math.PI) - (orbT - 0.5) * 0.06;

        this.camera.basePosition.set(camX, camY, camZ);
        this.camera.baseTarget.set(0, -0.02, -0.55);
        this.camera.fov = 26 + 5 * flyT - 2 * Math.sin(orbT * Math.PI);
        this.camera.updateProjectionMatrix();

        // Update shattered stone rings (naturally part & pass behind camera)
        const now = Fe.time;
        this.rings.forEach((rg, idx) => {
            const distAhead = camZ - rg.baseZ;
            rg.mesh.visible = distAhead > -0.35 && p < 0.55;
            rg.mesh.rotation.z = rg.baseRotZ + now * rg.speed + flyT * (idx === 0 ? 0.65 : -0.85);
            if (rg.mesh.material && rg.mesh.material.uniforms && rg.mesh.material.uniforms.uAlpha) {
                rg.mesh.material.uniforms.uAlpha.value = ie.smoothstep(-0.2, 0.7, distAhead);
            }
        });

        // Chapter typography softly appears inside ring aperture & dissolves completely before lens passes
        const chapIn = ie.smoothstep(0.08, 0.16, p);
        const chapOut = 1.0 - ie.smoothstep(0.21, 0.27, p);
        const chapA = chapIn * chapOut;
        if (this.chapterGroup) {
            this.chapterGroup.visible = chapA > 0.01;
            this._chapterMeshes.forEach(m => {
                if (m.material && m.material.uniforms) m.material.uniforms.uOpacity.value = chapA;
            });
        }

        // Scroll-driven seamless 100k particle morph between Project 01 (BettaFish) and Project 02 (AI Workflow)
        if (p > 0.38 && p < 0.95) {
            const desired = p >= 0.64 ? 1 : 0;
            if (desired !== this.activeIdx) {
                this.switchActiveProject(desired, !1);
            }
        }

        // Particle sculpture visibility, fluid interaction & mist reveal
        const partAlpha = ie.smoothstep(0.22, 0.42, p) * (1.0 - ie.smoothstep(0.88, 0.98, p));
        const showNoise = (1.0 - ie.smoothstep(0.26, 0.44, p)) + ie.smoothstep(0.86, 0.97, p);
        const interact = ie.smoothstep(0.38, 0.46, p) * (1.0 - ie.smoothstep(0.84, 0.92, p));
        if (this.particles) {
            this.particles.update(interact, partAlpha, ie.clamp(showNoise, 0, 1));
        }

        // Minimalist HUD fade
        const hudVis = ie.smoothstep(0.38, 0.46, p) * (1.0 - ie.smoothstep(0.85, 0.93, p));
        const hideForDetail = this.controller && this.controller.isDetailOpen ? 0 : 1;
        const finalHud = hudVis * hideForDetail;
        if (this.hudGroup) this.hudGroup.visible = finalHud > 0.01;
        if (this._hudLineMat) this._hudLineMat.opacity = finalHud * 0.72;
        if (this._arrowMat) this._arrowMat.opacity = finalHud * 0.52;
        this._projectHudSets.forEach((set, idx) => {
            if (!set.group.visible) return;
            set.meshes.forEach(m => {
                if (!m.material || !m.material.uniforms) return;
                m.material.uniforms.uOpacity.value = finalHud;
                m.material.uniforms.uShow1.value = ie.clamp(this._hudDecode.value * 1.4, 0, 1);
                m.material.uniforms.uShow2.value = this._hudDecode.value;
            });
        });

        this.bg.update(p);
        this.blurrytext.update(p);
        this.backgroundshapes.update(p);
    }
    autoCenter(e, t) {
        const stops = [0.22, 0.50, 0.78];
        let best = 1 / 0, diff = 0;
        stops.forEach(cp => {
            const d = cp - this.progress;
            if (Math.abs(d) < best) { best = Math.abs(d); diff = d; }
        });
        const delta = diff * (this.height + 1);
        const dur = ie.clamp(Math.abs(delta) * 5, 1.2, 2.2);
        e.centerScroll(e.scroll.y + delta, dur);
    }
    detailAnimationIn(delay = 0) {
        re.to(this.cameraZoom, { overwrite: !0, value: -1.15, duration: 1.15 + delay, ease: "power3.in" });
        re.to(this.camera, { touchAmount: 0, overwrite: !0, duration: 1.15 + delay });
    }
    detailAnimationOut() {
        re.to(this.cameraZoom, { overwrite: !0, value: 0, duration: 1.25, ease: "power3.out" });
        re.to(this.camera, { touchAmount: 1, overwrite: !0, duration: 1.25 });
    }
    resize() {
        this.camera.zoom = Math.min(1, q.screen.aspectRatio * 1.15);
        this.camera.updateProjectionMatrix();
    }
    dispose() {}
}
'''

NEW_VF_CLASS = r'''class VF{constructor(e,t){this.options={index:0,obj:"pudgy",scale:1,rand:Math.random(),...t},this.scene=e,this.ready=new Promise(s=>{this.isReady=s}),this.index=this.options.index,this.additionalRotationAmount={value:0},this.init()}async init(){const isProjDetail=this.options.obj.startsWith("project_detail_");const drcName=isProjDetail?(this.options.obj.endsWith("2")?"shattered_ring":"shattered_ring2"):this.options.obj;const mapName=isProjDetail?`${drcName}_color.ktx2`:`${this.options.obj}_dark_color.ktx2`;const e=await zt.load(`${drcName}.drc`);this.mesh=new Ce(e,new fe({uniformsGroups:[he.UBO],uniforms:{tMap:{value:le.load(mapName)},tNoise:{value:le.load("perlin-datatexture.ktx2","srgb-repeat")},tCaustics:{value:le.load("caustics.ktx2","srgb-repeat")},uDarkMul:{value:isProjDetail?0.55:1.0}},vertexShader:`
                //- edit
                ${ae}

                varying vec2 vUv;
                varying vec3 vPos;

                void main() {
                    vUv = uv;
                    vPos = position;
                    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
                }
            `,fragmentShader:`
                //- edit
                ${ae}
                ${Cr}

                varying vec2 vUv;
                varying vec3 vPos;

                uniform sampler2D tMap;
                uniform sampler2D tNoise;
                uniform sampler2D tCaustics;
                uniform float uDarkMul;

                void main() {
                    vec3 color = texture2D(tMap, vUv).rgb;
                    float noise = texture2D(tNoise, vPos.xy * 0.4 + vec2(-time * 0.1, time * 0.023)).r;
                    color *= mix(0.025, 0.15, noise) * uDarkMul;

                    float caustics = texture2D(tCaustics, vPos.xy * 1.5 + vec2(-time * 0.1, time * 0.023)).r;
                    caustics = min(caustics, texture2D(tCaustics, vPos.xy * 2.0 + vec2(time * 0.05, -time * 0.013)).r);
                    color += caustics * color.b * (uDarkMul < 0.9 ? 14.0 : 30.0);

                    gl_FragColor = vec4(color, 1.0);
                }
            `})),this.mesh.name="object",this.mesh.frustumCulled=!1,this.mesh.scale.setScalar(this.options.scale),isProjDetail&&this.mesh.rotation.set(0.18,0.22,0),q.devScene&&(this.mesh.visible=this.index===0),this.mesh.onBeforeRender=()=>{const s=.035*this.additionalRotationAmount.value,n=Math.sin(Fe.time*.3+this.options.rand*12.423)*s*Math.sign(this.options.rand-.5),r=Math.sin(Fe.time*.3+this.options.rand*42.987)*s*Math.sign(this.options.rand-.5),a=Math.sin(Fe.time*.3+this.options.rand*2.53)*s*Math.sign(this.options.rand-.5);isProjDetail?this.mesh.rotation.set(0.18+n,0.22+r,Fe.time*.04+a):this.mesh.rotation.set(n,r,a)},this.scene.add(this.mesh),this.isReady()}}'''


def replace_span(text: str, start_anchor: str, end_anchor: str, replacement: str, keep_end: bool = True) -> str:
    i1 = text.find(start_anchor)
    assert i1 != -1, f"Missing start anchor: {start_anchor[:80]!r}"
    i2 = text.find(end_anchor, i1)
    assert i2 != -1, f"Missing end anchor: {end_anchor[:80]!r}"
    if keep_end:
        return text[:i1] + replacement + text[i2:]
    return text[:i1] + replacement + text[i2 + len(end_anchor):]


def main():
    # Start cleanly from v6 baseline (zero v7 artifacts)
    app = (ROOT / "assets/App3D-aurora-preview-v6.js").read_text(encoding="utf-8")

    # 1. Replace Be.cubes (2 frozen internships + 2 fluid-particle projects)
    app = replace_span(app, 'cubes:[{title:"PROJECT_CO_01', ',links:[{title:', NEW_CUBES_CONFIG, keep_end=True)

    # 1b. Disable PDF resume jump on bottom pedestal while keeping entry & hint feedback
    resume_link_old = '{title:"个人简历",url:"./assets/resume-guishaocong.pdf",hint:"桂少聪-AI产品经理-简历.pdf · 点击打开 / 下载",activeHint:"已打开简历 PDF · 如未弹出请允许弹窗",vdb:"cv_doc_64",scale:1.25}'
    resume_link_new = '{title:"个人简历",url:"",hint:"桂少聪 · 简历 PDF 版本后续开放",activeHint:"简历 PDF 后续开放 · 请通过邮箱 / 微信联系",vdb:"cv_doc_64",scale:1.25}'
    assert resume_link_old in app, "Missing resume_link_old anchor"
    app = app.replace(resume_link_old, resume_link_new, 1)

    trigger_action_old = 'if(r&&r.copyText){this.copyAndNotify(r)}else if(r&&r.url){const w=window.open(r.url,"_blank");if(w){try{w.opener=null}catch(e){}w.focus&&w.focus()}else{const a=document.createElement("a");a.href=r.url,a.target="_blank",a.rel="noopener",document.body.appendChild(a),a.click(),a.remove()}Q.emit("webgl_play_audio","ui-long"),this.texts&&this.texts.triggerCopied&&this.texts.triggerCopied()}'
    trigger_action_new = 'if(r&&r.copyText){this.copyAndNotify(r)}else if(r&&r.url){const w=window.open(r.url,"_blank");if(w){try{w.opener=null}catch(e){}w.focus&&w.focus()}else{const a=document.createElement("a");a.href=r.url,a.target="_blank",a.rel="noopener",document.body.appendChild(a),a.click(),a.remove()}Q.emit("webgl_play_audio","ui-long"),this.texts&&this.texts.triggerCopied&&this.texts.triggerCopied()}else if(r&&r.activeHint){Q.emit("webgl_play_audio","ui-long"),this.texts&&this.texts.triggerCopied&&this.texts.triggerCopied()}'
    assert trigger_action_old in app, "Missing trigger_action_old anchor"
    app = app.replace(trigger_action_old, trigger_action_new, 1)

    # 2. Update Hero Copy, Quadrants (Growth/Ops Priority) & Quadrant click-through
    for old_txt, new_txt in HERO_COPY_PATCHES:
        assert old_txt in app, f"Missing HERO_COPY_PATCHES anchor: {old_txt[:70]!r}"
        app = app.replace(old_txt, new_txt, 1)

    assert HERO_QUAD_OLD in app, "Missing HERO_QUAD_OLD"
    app = app.replace(HERO_QUAD_OLD, HERO_QUAD_NEW, 1)
    assert HERO_CLICK_OLD in app, "Missing HERO_CLICK_OLD"
    app = app.replace(HERO_CLICK_OLD, HERO_CLICK_NEW, 1)

    # 2c. Upgrade Detail Room text hierarchy, typography scale & optical MSDF weight
    detail_margin_old = 'this.width=500,this.scrollMargin=65,this.scrollMax=0'
    detail_margin_new = 'this.width=760,this.scrollMargin=34,this.scrollMax=0'
    assert detail_margin_old in app, "Missing detail_margin_old anchor"
    app = app.replace(detail_margin_old, detail_margin_new, 1)

    detail_msdf_old = 'alpha *= msdf(tMap, uv);\n                        alpha *= uOpacity;'
    detail_msdf_new = 'float sd = median(tMap, uv); float d = max(fwidth(sd), 0.0001); alpha *= smoothstep(-d, d, sd + 0.032);\n                        alpha *= uOpacity;'
    assert app.count(detail_msdf_old) >= 2, f"Expected >=2 detail_msdf_old, found {app.count(detail_msdf_old)}"
    app = app.replace(detail_msdf_old, detail_msdf_new)

    detail_init_old = 'const e=Be.cubes[this.index].interior,t={font:"IBMPlexMono-Medium",color:"#ffffff",width:4,align:"left",lineHeight:1,size:14,baseOffset:-.65};this.elements.push(new Yh({parent:this,text:e.title,options:{...t,color:Be.colorProjectTitle}}),new Yh({parent:this,text:e.content,options:{...t,color:Be.colorProjectText}}),new Yh({parent:this,text:e.socialTitle,options:{...t,color:Be.colorProjectTitle}}),new ey({parent:this,links:e.social,options:{...t,color:Be.colorProjectText}}),new Yh({parent:this,text:e.linkTitle,options:{...t,color:Be.colorProjectTitle}}),new ey({parent:this,links:e.links,options:{...t,color:Be.colorProjectText}}))'
    detail_init_new = 'const e=Be.cubes[this.index].interior,t={font:"IBMPlexMono-Medium",color:"#ffffff",width:4,align:"left",lineHeight:1.08,size:14,baseOffset:-.65};const _push=(el,gap,mul=1)=>{el._gapAfter=gap;el._sizeMul=mul;this.elements.push(el);return el;};_push(new Yh({parent:this,text:e.title,options:{...t,color:"#9FB3CC"}}),e.subtitle?5:10,0.88);e.subtitle&&_push(new Yh({parent:this,text:e.subtitle,options:{...t,color:"#D4E2F4"}}),10,0.94);e.highlight&&_push(new Yh({parent:this,text:e.highlight,options:{...t,color:"#FFFFFF"}}),18,1.10);if(Array.isArray(e.sections)&&e.sections.length){e.sections.forEach((sec,si)=>{_push(new Yh({parent:this,text:sec.heading,options:{...t,color:"#B4D7FF"}}),4,1.02);_push(new Yh({parent:this,text:sec.body,options:{...t,color:"#D2DBE8"}}),si===e.sections.length-1?18:12,0.95);})}else{_push(new Yh({parent:this,text:e.content,options:{...t,color:"#D2DBE8"}}),18,1.0)}_push(new Yh({parent:this,text:e.socialTitle,options:{...t,color:"#9FB3CC"}}),5,0.88);_push(new ey({parent:this,links:e.social,options:{...t,color:"#E6F0FF"}}),10,0.94);_push(new Yh({parent:this,text:e.linkTitle,options:{...t,color:"#9FB3CC"}}),5,0.88);_push(new ey({parent:this,links:e.links,options:{...t,color:"#E6F0FF"}}),0,0.94)'
    assert detail_init_old in app, "Missing detail_init_old anchor"
    app = app.replace(detail_init_old, detail_init_new, 1)

    ey_click_old = 'onClick:e=>{const t=e.interactions[0].object._index;window.open(this.els[t].data.link,"_blank").focus()}'
    ey_click_new = 'onClick:e=>{const t=e.interactions[0].object._index;const lnk=this.els[t].data.link;if(!lnk)return;const w=window.open(lnk,"_blank");w&&w.focus&&w.focus()}'
    assert ey_click_old in app, "Missing ey_click_old anchor"
    app = app.replace(ey_click_old, ey_click_new, 1)

    detail_show_old = 'show(){this.group.visible=!0,this.scrollY=0,this.scrollTargetY=0;let e=0;this.elements.forEach((t,s)=>{var a;const n=!!t.text,r=n?t.text.length>100?.75:.25:.3;t.show(r,e),e+=n&&t.text.length>100?.3:.1,(a=t.interaction)==null||a.enable()})}'
    detail_show_new = 'show(){this.group.visible=!0,this.scrollY=0,this.scrollTargetY=0;let e=0;this.elements.forEach((t,s)=>{var a;const n=!!t.text,r=n?t.text.length>100?.48:.24:.24;t.show(r,e),e=Math.min(e+0.055,0.55),(a=t.interaction)==null||a.enable()})}'
    assert detail_show_old in app, "Missing detail_show_old anchor"
    app = app.replace(detail_show_old, detail_show_new, 1)

    detail_size_old = 'const e=this.scene.small?18:24,t=500,s=20;this.width=Math.min(q.screen.width-s*2,t);const n=25,r=Math.max(s,(q.screen.width-this.width)*.5);'
    detail_size_new = 'const e=this.scene.mobile?20:this.scene.small?26:30,t=this.scene.mobile?480:this.scene.small?760:860,s=24;this.width=Math.min(q.screen.width-s*2,t);const n=18,r=Math.max(s,(q.screen.width-this.width)*.5);'
    assert detail_size_old in app, "Missing detail_size_old anchor"
    app = app.replace(detail_size_old, detail_size_new, 1)

    ey_show_old = 'show(e=1,t=0){return Promise.all(this.els.map((s,n)=>s.show(.5,t+n*.1)))}'
    ey_show_new = 'show(e=1,t=0){return Promise.all(this.els.map((s,n)=>s.show(.24,t+n*.06)))}'
    assert ey_show_old in app, "Missing ey_show_old anchor"
    app = app.replace(ey_show_old, ey_show_new, 1)

    detail_resize_full_old = 'this.ready.then(()=>Promise.all(this.elements.map(a=>a.resize({size:e,width:this.width}))).then(()=>{const a=this.elements.reduce((c,h)=>c+h.mesh.size.y,0)+n*(this.elements.length-1);let o=0;if(this.scrollMax=Math.max(0,a-(q.screen.height-this.scrollMargin*4)),this.scrollMax>0){o=this.scrollMargin*2;const c=this.scrollMax===0?0:this.scrollY/this.scrollMax;this.scrollY=c*this.scrollMax,this.scrollTargetY=this.scrollY}else o=(q.screen.height-a)*.5,this.scrollY=0,this.scrollTargetY=0;let l=o;this.elements.forEach(c=>{c.mesh.position.set(r,-l,0),l+=c.mesh.size.y+n})}))'
    detail_resize_full_new = 'this.ready.then(()=>Promise.all(this.elements.map(a=>a.resize({size:e*(a._sizeMul||1),width:this.width}))).then(()=>{const a=this.elements.reduce((c,h,hi)=>c+h.mesh.size.y+(hi<this.elements.length-1?(h._gapAfter??n):0),0);let o=0;if(this.scrollMax=Math.max(0,a-(q.screen.height-this.scrollMargin*4)),this.scrollMax>0){o=this.scrollMargin*2;const c=this.scrollMax===0?0:this.scrollY/this.scrollMax;this.scrollY=c*this.scrollMax,this.scrollTargetY=this.scrollY}else o=(q.screen.height-a)*.5,this.scrollY=0,this.scrollTargetY=0;let l=o;this.elements.forEach((c,ci)=>{c.mesh.position.set(r,-l,0),l+=c.mesh.size.y+(ci<this.elements.length-1?(c._gapAfter??n):0)})}))'
    assert detail_resize_full_old in app, "Missing detail_resize_full_old anchor"
    app = app.replace(detail_resize_full_old, detail_resize_full_new, 1)

    ey_icon_old = 'const a=this.parent.scene.small?12:18,o=n.mesh.size.x+a,l=n.mesh.size.y;t+o>this.parent.width&&(t=0,s-=l+10),n.mesh.position.set(t,s,0),n.icon.scale.set(a,a,1),n.icon.position.set(n.mesh.size.x-a+5,0,0)'
    ey_icon_new = 'const a=this.parent.scene.mobile?13:this.parent.scene.small?18:21,o=n.mesh.size.x+a+8,l=n.mesh.size.y;t+o>this.parent.width&&(t=0,s-=l+10),n.mesh.position.set(t,s,0),n.icon.scale.set(a,a,1),n.icon.position.set(n.mesh.size.x+7,0,0)'
    assert ey_icon_old in app, "Missing ey_icon_old anchor"
    app = app.replace(ey_icon_old, ey_icon_new, 1)

    # 2b. Refine Hero & Global Corner HUD typography back to crisp igloo.inc editorial scale
    l3_opt_old = 'this.options={manifestoWidth:1.05,copyrightWidth:1.25,align:"right",lineHeight:.90,size:.116}'
    l3_opt_new = 'this.options={manifestoWidth:1.15,copyrightWidth:1.35,align:"right",lineHeight:.92,size:.09}'
    assert l3_opt_old in app, "Missing L3 options anchor"
    app = app.replace(l3_opt_old, l3_opt_new, 1)

    l3_rsz_old = 's=t?215:e?265:315,n=s,r=t?Be.gridSizeMobile:e?Be.gridSizeLow:Be.gridSize,a=t?Be.topMarginMobile:e?Be.topMarginLow:Be.topMargin;Si.positionUI({camera:this.scene.camera,mesh:this.title,x:q.screen.width-r,y:a+this.title.size.y*.82*n,width:s,height:n}),Si.positionUI({camera:this.scene.camera,mesh:this.text,x:q.screen.width-r,y:a+this.title.size.y*2.15*n,width:s,height:n});const l=(e?160:200)*.21,c=a+l+this.copyright.size.y*1.25*s;Si.positionUI({camera:this.scene.camera,mesh:this.copyright,x:r,y:c,width:s,height:s}),Si.positionUI({camera:this.scene.camera,mesh:this.rights,x:r,y:c+this.copyright.size.y*1.48*s,width:s,height:s})'
    l3_rsz_new = 's=t?170:e?202:244,n=s,r=t?Be.gridSizeMobile:e?Be.gridSizeLow:Be.gridSize,a=t?Be.topMarginMobile:e?Be.topMarginLow:Be.topMargin;Si.positionUI({camera:this.scene.camera,mesh:this.title,x:q.screen.width-r,y:a+this.title.size.y*.82*n,width:s,height:n}),Si.positionUI({camera:this.scene.camera,mesh:this.text,x:q.screen.width-r,y:a+this.title.size.y*2.20*n,width:s,height:n});const l=(t?120:e?138:168)*.21,c=a+l+this.copyright.size.y*1.32*s;Si.positionUI({camera:this.scene.camera,mesh:this.copyright,x:r,y:c,width:s,height:s}),Si.positionUI({camera:this.scene.camera,mesh:this.rights,x:r,y:c+this.copyright.size.y*1.52*s,width:s,height:s})'
    assert l3_rsz_old in app, "Missing L3 render anchor"
    app = app.replace(l3_rsz_old, l3_rsz_new, 1)

    lf_rsz_old = 'resize(){const e=this.scene.mobile?140:this.scene.small?160:200,t=e*.21;this.mesh.scale.set(e,t,1),this.mesh.position.set(this.scene.meshMarginLeft,-this.scene.meshMarginTop,0)}}class FF{'
    lf_rsz_new = 'resize(){const e=this.scene.mobile?120:this.scene.small?138:168,t=e*.21;this.mesh.scale.set(e,t,1),this.mesh.position.set(this.scene.meshMarginLeft,-this.scene.meshMarginTop,0)}}class FF{'
    assert lf_rsz_old in app, "Missing LF resize anchor"
    app = app.replace(lf_rsz_old, lf_rsz_new, 1)

    ff_opt_old = 'this.options={width:1.45,align:"left",lineHeight:.88,size:.114}'
    ff_opt_new = 'this.options={width:1.55,align:"left",lineHeight:.88,size:.09}'
    assert ff_opt_old in app, "Missing FF options anchor"
    app = app.replace(ff_opt_old, ff_opt_new, 1)

    ff_rsz_old = 'resize(){const e=this.scene.small?225:280,t=e;this.message.scale.set(e,t,1),this.message.position.set(this.scene.meshMarginLeft,-q.screen.height+this.scene.meshMarginTop+this.message.size.y*1.85*t+14,0)}}class NF{'
    ff_rsz_new = 'resize(){const e=this.scene.small?182:226,t=e;this.message.scale.set(e,t,1),this.message.position.set(this.scene.meshMarginLeft,-q.screen.height+this.scene.meshMarginTop+this.message.size.y*1.85*t+12,0)}}class NF{'
    assert ff_rsz_old in app, "Missing FF resize anchor"
    app = app.replace(ff_rsz_old, ff_rsz_new, 1)

    nf_opt_old = 'this.options={width:1.2,align:"left",lineHeight:.85,size:.114}'
    nf_opt_new = 'this.options={width:1.2,align:"left",lineHeight:.85,size:.09}'
    assert nf_opt_old in app, "Missing NF options anchor"
    app = app.replace(nf_opt_old, nf_opt_new, 1)

    nf_rsz_old = 'resize(){const e=this.scene.small?21:25;this.icon.scale.set(e,e,1),this.icon.position.set(this.scene.meshMarginLeft,-q.screen.height+this.scene.meshMarginTop+e*.7,0);const t=this.scene.small?225:280,s=t;'
    nf_rsz_new = 'resize(){const e=this.scene.small?17:21;this.icon.scale.set(e,e,1),this.icon.position.set(this.scene.meshMarginLeft,-q.screen.height+this.scene.meshMarginTop+e*.7,0);const t=this.scene.small?182:226,s=t;'
    assert nf_rsz_old in app, "Missing NF resize anchor"
    app = app.replace(nf_rsz_old, nf_rsz_new, 1)

    # 3. Filter aF (cubes scene) so it ONLY renders the 2 original frozen internship cubes
    af_cubes_old = 'this.options={cubes:Be.cubes,verticalOffset:-5.75}'
    af_cubes_new = 'this.options={cubes:Be.cubes.filter(c=>c.kind!=="project"),verticalOffset:-5.75}'
    assert af_cubes_old in app, "Missing aF cubes anchor"
    app = app.replace(af_cubes_old, af_cubes_new, 1)

    # Expand YL title and date width slightly for clean bilingual wrapping
    yl_old = 'text:this.parent.options.title.toUpperCase(),width:1,align:"left"'
    yl_new = 'text:this.parent.options.title.toUpperCase(),width:1.45,align:"left"'
    assert yl_old in app, "Missing YL width anchor"
    app = app.replace(yl_old, yl_new, 1)

    date_w_old = 'this.parent.options.date.replaceAll("/",".")}\n${(s?Be.click:Be.clickDisabled).toUpperCase()}`,width:1,align:"right"'
    date_w_new = 'this.parent.options.date.replaceAll("/",".")}\n${(s?Be.click:Be.clickDisabled).toUpperCase()}`,width:1.45,align:"right"'
    assert date_w_old in app, "Missing cube date width anchor"
    app = app.replace(date_w_old, date_w_new, 1)

    # 4. Upgrade VF so project detail rooms render sculpted shattered_ring dark caustic silhouettes
    app = replace_span(app, "class VF{", "class WF{", NEW_VF_CLASS, keep_end=True)

    # 5. Register Plan8ProjectScene right between cubes (aF) and entry (UF) in ty
    ty_old = 'const ty={igloo:F3,cubes:aF,entry:UF};'
    ty_new = PLAN8_PROJECT_SCENE + '\nconst ty={igloo:F3,cubes:aF,projects:Plan8ProjectScene,entry:UF};'
    assert ty_old in app, "Missing ty anchor"
    app = app.replace(ty_old, ty_new, 1)

    # 6. Update jF (main controller) to route detail views cleanly across both cubes[1] and projects[2]
    # 6a. tCubes & uInCubes in jF.render()
    render_cubes_old = 'this.material.uniforms.tCubes.value=this.scrollComposers[1].readBuffer.texture,this.material.uniforms.uInCubes.value=o===1,'
    render_cubes_new = 'const _dSrc=(o===1||o===2)?o:(Be.cubes[this.detailIndex]&&Be.cubes[this.detailIndex].kind==="project"?2:1);this.material.uniforms.tCubes.value=this.scrollComposers[_dSrc].readBuffer.texture,this.material.uniforms.uInCubes.value=(o===1||o===2||this.isDetailOpen),'
    assert render_cubes_old in app, "Missing jF render tCubes anchor"
    app = app.replace(render_cubes_old, render_cubes_new, 1)

    # 6b. centerDetailScene(e=1)
    center_old = 'centerDetailScene(e=1){const t=this.scrollComposers[1].passes[0].scene;(!this.scrollComposers[1].passes[0].scene.isSceneVisible||e===0)&&(this.scroll.y=this.scrollComposers[0].passes[0].scene.height,this.resize(),t.progress=1/(t.height+1));const n=(t.cubes[this.detailIndex].options.centeredProgress-t.progress)*(t.height+1),r=Math.abs(n);let a=0;return e>0&&(a=ie.ease(ie.fit(r,0,.2,.05,1),"expo.out")*1.5),this.centerScroll(this.scroll.y+n,a),a}'
    center_new = 'getDetailSceneIndex(){const it=Be.cubes[this.detailIndex];return it&&it.kind==="project"?2:1}centerDetailScene(e=1){const sIdx=this.getDetailSceneIndex();const t=this.scrollComposers[sIdx].passes[0].scene;let topY=0;for(let k=0;k<sIdx;k++)topY+=this.scrollComposers[k].passes[0].scene.height;if(!t.isSceneVisible||e===0){this.scroll.y=topY,this.resize(),t.progress=1/(t.height+1)}let targetP=1/(t.height+1);if(sIdx===2){const it=Be.cubes[this.detailIndex];const slot=it&&typeof it.projectSlot=="number"?it.projectSlot:0;t.switchActiveProject(slot,!0);targetP=t.getStopProgressForSlot(slot)}else{const it=Be.cubes[this.detailIndex];const cObj=t.cubes.find(c=>c.options.hash===(it&&it.hash))||t.cubes[0];targetP=cObj.options.centeredProgress}const n=(targetP-t.progress)*(t.height+1),r=Math.abs(n);let a=0;return e>0&&(a=ie.ease(ie.fit(r,0,.2,.05,1),"expo.out")*1.5),this.centerScroll(this.scroll.y+n,a),a}'
    assert center_old in app, "Missing centerDetailScene anchor"
    app = app.replace(center_old, center_new, 1)

    # 6c. navigateToSection detailAnimationIn/Out & visibility guard
    nav_out_old = 'this.scrollComposers[1].passes[0].scene.detailAnimationOut()'
    nav_out_new = 'this.scrollComposers[this._lastDetailSceneIdx||1].passes[0].scene.detailAnimationOut()'
    assert nav_out_old in app, "Missing detailAnimationOut anchor"
    app = app.replace(nav_out_old, nav_out_new, 1)

    nav_guard_old = '!this.isFirstNavigation&&!this.scrollComposers[1].passes[0].scene.isSceneVisible'
    nav_guard_new = '!this.isFirstNavigation&&!this.scrollComposers[1].passes[0].scene.isSceneVisible&&!this.scrollComposers[2].passes[0].scene.isSceneVisible&&!this.scrollComposers[0].passes[0].scene.isSceneVisible'
    assert nav_guard_old in app, "Missing nav guard anchor"
    app = app.replace(nav_guard_old, nav_guard_new, 1)

    nav_in1_old = 'this.scrollComposers[1].passes[0].scene.detailAnimationIn(0)'
    nav_in1_new = '(this._lastDetailSceneIdx=this.getDetailSceneIndex(),this.scrollComposers[this._lastDetailSceneIdx].passes[0].scene.detailAnimationIn(0))'
    assert nav_in1_old in app, "Missing detailAnimationIn(0) anchor"
    app = app.replace(nav_in1_old, nav_in1_new, 1)

    nav_in2_old = 'this.scrollComposers[1].passes[0].scene.detailAnimationIn(a)'
    nav_in2_new = '(this._lastDetailSceneIdx=this.getDetailSceneIndex(),this.scrollComposers[this._lastDetailSceneIdx].passes[0].scene.detailAnimationIn(a))'
    assert nav_in2_old in app, "Missing detailAnimationIn(a) anchor"
    app = app.replace(nav_in2_old, nav_in2_new, 1)

    # 7. Update bundle self-reference
    assert "./index-aurora-preview-v6.js" in app
    app = app.replace("./index-aurora-preview-v6.js", "./index-aurora-preview-v8.js")

    (ROOT / "assets/App3D-aurora-preview-v8.js").write_text(app, encoding="utf-8")

    # 8. Create index-aurora-preview-v8.js and point index.html to v8
    v6_index = (ROOT / "assets/index-aurora-preview-v6.js").read_text(encoding="utf-8")
    assert "App3D-aurora-preview-v6.js" in v6_index
    (ROOT / "assets/index-aurora-preview-v8.js").write_text(
        v6_index.replace("App3D-aurora-preview-v6.js", "App3D-aurora-preview-v8.js"),
        encoding="utf-8"
    )

    html_v6 = (ROOT / "index.before-v7.html").read_text(encoding="utf-8")
    assert "index-aurora-preview-v6.js" in html_v6
    html_v8 = (
        html_v6
        .replace("index-aurora-preview-v6.js", "index-aurora-preview-v8.js")
        .replace("桂少聪的个人网站 — 占位文案，作品与联系方式的展示站点。", "桂少聪个人主页｜涵盖蔚来用户增长、汇川研发协同提效、微舆多 Agent 评测与 AI 工作流实战。")
        .replace("桂少聪 · 个人网站", "桂少聪 · 产品运营 / AI 产品")
    )
    (ROOT / "index.html").write_text(html_v8, encoding="utf-8")

    # 9. Add App3D-aurora-preview-v8.js to rebuild_font.sh
    rebuild = (ROOT / "rebuild_font.sh").read_text(encoding="utf-8")
    if "App3D-aurora-preview-v8.js" not in rebuild:
        rebuild = rebuild.replace(
            "'assets/App3D-aurora-preview-v7.js',",
            "'assets/App3D-aurora-preview-v7.js',\n    'assets/App3D-aurora-preview-v8.js',"
        )
        (ROOT / "rebuild_font.sh").write_text(rebuild, encoding="utf-8")

    print("Successfully built Plan v8 (100% igloo-native Shattered-Ring + 100K Particle Gallery)")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
