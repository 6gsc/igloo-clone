#!/usr/bin/env python3
"""Build Form A (Spatial Telemetry + Polar Particles + Enhanced Bottom Entries) directly in igloo-clone."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GROUND_UNIFORM_ADD = (
    'tMap:{value:le.load("igloo/ground_color.ktx2","srgb")}',
    'tMap:{value:le.load("igloo/ground_color.ktx2","srgb")},tCleanSnow:{value:le.load("igloo/ground_sansigloo_color.ktx2","srgb")}'
)
GROUND_DECL_ADD = (
    'uniform sampler2D tMap;\n                uniform sampler2D tWind;\n                uniform sampler2D tGroundGlow;',
    'uniform sampler2D tMap;\n                uniform sampler2D tCleanSnow;\n                uniform sampler2D tWind;\n                uniform sampler2D tGroundGlow;'
)
GROUND_COLOR_ADD = (
    'vec3 terrainColor = texture2D(tMap, vUv).rgb;',
    """vec3 terrainColor = texture2D(tMap, vUv).rgb;
                    float oldImprint = 1.0 - smoothstep(3.35, 4.7, length(vWorldPos.xz));
                    terrainColor = mix(terrainColor, texture2D(tCleanSnow, vUv).rgb, oldImprint);
                    vec2 localFeet = vec2(dot(vWorldPos.xz, vec2(0.95233, 0.30506)), dot(vWorldPos.xz, vec2(-0.30506, 0.95233)));
                    vec2 coreUV = vec2((localFeet.x + 0.02) / 1.75, (localFeet.y - 0.02) / 0.90);
                    vec2 skirtUV = vec2((localFeet.x + 0.02) / 3.00, (localFeet.y - 0.02) / 1.55);
                    float auroraCore = exp(-dot(coreUV, coreUV));
                    float auroraSkirt = exp(-dot(skirtUV, skirtUV));
                    float pulse = sin(localFeet.x * 1.5 - time * 0.9) * 0.5 + 0.5;
                    vec3 glacialReflection = mix(vec3(0.48, 0.70, 0.98), vec3(0.70, 0.86, 1.00), pulse);
                    terrainColor *= 1.0 - 0.14 * auroraCore;
                    terrainColor += glacialReflection * (auroraCore * 0.16 + auroraSkirt * 0.08);"""
)
U3_FRAG_HIDE = (
    'color += (1.0 - smoothstep(-1.5, 1.0, vPos.y)) * vBounce * vec3(0.8, 0.9, 1.0) * 0.25;\n\n                    gl_FragColor = vec4(color, 1.0);',
    'discard;\n                    gl_FragColor = vec4(0.0);'
)
OUTLINE_HIDE = (
    'igloo_outline.drc"),t=new E3({color:"#a7b2d6",opacity:.3',
    'igloo_outline.drc"),t=new E3({color:"#a7b2d6",opacity:.0'
)
COPY_REPLACEMENTS = [
    (
        'manifesto:{title:"////// Manifesto",text:"这里是桂少聪的个人网站。作品、实验与想法都会在这里生长，用技术把有趣的东西做出来。正式介绍稍后补上。"}',
        'manifesto:{title:"////// Profile",text:"习惯从一线业务卡点切入，\\n擅长用流程重构、数据漏斗\\n与评测体系驱动产品落地。"}'
    ),
    (
        'rights:`桂少聪\\n版权所有 · 占位版`',
        'rights:`27届本科 · 专业 Top 5%\\n信管(计算机×商分) · 一周到岗`'
    ),
    (
        'scroll:"向下滚动，开始探索。"',
        'scroll:"向下滚动 · 查看项目拆解与简历"'
    ),
    (
        'this.optionsTexture.needsUpdate=!0,this.introDisplacementModulator.value===1&&((r=this.plexus)==null||r.update())',
        'this.optionsTexture.needsUpdate=!0,this._updateAuroraWheel(s)'
    ),
    (
        'links:[{title:"个人简历",url:"./assets/resume-guishaocong.pdf",vdb:"cv_doc_64",scale:1.25},{title:"邮箱联系",url:"mailto:EurusGui@qq.com",vdb:"mail_64",scale:1.25},{title:"电话/微信",url:"tel:18504205236",copyText:"18504205236",vdb:"phone_wechat_64",scale:1.22}]',
        'links:[{title:"个人简历",url:"./assets/resume-guishaocong.pdf",hint:"桂少聪-AI产品经理-简历.pdf · 点击打开 / 下载",activeHint:"已打开简历 PDF · 如未弹出请允许弹窗",vdb:"cv_doc_64",scale:1.25},{title:"邮箱联系",url:"mailto:EurusGui@qq.com",copyText:"EurusGui@qq.com",hint:"EurusGui@qq.com · 点击复制邮箱",activeHint:"已复制 EurusGui@qq.com",vdb:"mail_64",scale:1.25},{title:"电话/微信",url:"tel:18504205236",copyText:"18504205236",hint:"18504205236 · 点击复制（微信同号）",activeHint:"已复制 18504205236",vdb:"phone_wechat_64",scale:1.22}]'
    ),
    # Boost L3 corner typography size & crisp optical MSDF weight
    (
        'this.options={manifestoWidth:.75,copyrightWidth:.9,align:"right",lineHeight:.8,size:.09}',
        'this.options={manifestoWidth:1.05,copyrightWidth:1.25,align:"right",lineHeight:.90,size:.116}'
    ),
    (
        'render(){const e=q.screen.width<Be.breakpointW||q.screen.height<Be.breakpointH,t=q.screen.width<Be.breakPointMobile||q.screen.height<Be.breakPointMobile,s=t?175:e?200:250,n=s,r=t?Be.gridSizeMobile:e?Be.gridSizeLow:Be.gridSize,a=t?Be.topMarginMobile:e?Be.topMarginLow:Be.topMargin;Si.positionUI({camera:this.scene.camera,mesh:this.title,x:q.screen.width-r,y:a+this.title.size.y*.75*n,width:s,height:n}),Si.positionUI({camera:this.scene.camera,mesh:this.text,x:q.screen.width-r,y:a+this.title.size.y*2.25*n,width:s,height:n});const l=(e?160:200)*.21,c=a+l+this.copyright.size.y*1.25*s;Si.positionUI({camera:this.scene.camera,mesh:this.copyright,x:r,y:c,width:s,height:s}),Si.positionUI({camera:this.scene.camera,mesh:this.rights,x:r,y:c+this.copyright.size.y*1.5*s,width:s,height:s})}',
        'render(){const e=q.screen.width<Be.breakpointW||q.screen.height<Be.breakpointH,t=q.screen.width<Be.breakPointMobile||q.screen.height<Be.breakPointMobile,s=t?215:e?265:315,n=s,r=t?Be.gridSizeMobile:e?Be.gridSizeLow:Be.gridSize,a=t?Be.topMarginMobile:e?Be.topMarginLow:Be.topMargin;Si.positionUI({camera:this.scene.camera,mesh:this.title,x:q.screen.width-r,y:a+this.title.size.y*.82*n,width:s,height:n}),Si.positionUI({camera:this.scene.camera,mesh:this.text,x:q.screen.width-r,y:a+this.title.size.y*2.15*n,width:s,height:n});const l=(e?160:200)*.21,c=a+l+this.copyright.size.y*1.25*s;Si.positionUI({camera:this.scene.camera,mesh:this.copyright,x:r,y:c,width:s,height:s}),Si.positionUI({camera:this.scene.camera,mesh:this.rights,x:r,y:c+this.copyright.size.y*1.48*s,width:s,height:s})}'
    ),
    # Boost FF bottom-left scroll prompt size & spacing above Sound:
    (
        'class FF{constructor(e){this.scene=e,this.ready=new Promise(t=>{this.isReady=t}),this.options={width:.6,align:"left",lineHeight:.8,size:.09}',
        'class FF{constructor(e){this.scene=e,this.ready=new Promise(t=>{this.isReady=t}),this.options={width:1.45,align:"left",lineHeight:.88,size:.114}'
    ),
    (
        'resize(){const e=this.scene.small?180:230,t=e;this.message.scale.set(e,t,1),this.message.position.set(this.scene.meshMarginLeft,-q.screen.height+this.scene.meshMarginTop+this.message.size.y*1.75*t,0)}',
        'resize(){const e=this.scene.small?225:280,t=e;this.message.scale.set(e,t,1),this.message.position.set(this.scene.meshMarginLeft,-q.screen.height+this.scene.meshMarginTop+this.message.size.y*1.85*t+14,0)}'
    ),
    # Boost NF bottom-left Sound: On/Off size
    (
        'class NF{constructor(e){this.scene=e,this.ready=new Promise(t=>{this.isReady=t}),this.options={width:1,align:"left",lineHeight:.8,size:.09}',
        'class NF{constructor(e){this.scene=e,this.ready=new Promise(t=>{this.isReady=t}),this.options={width:1.2,align:"left",lineHeight:.85,size:.114}'
    ),
    (
        'resize(){const e=this.scene.small?18:22;this.icon.scale.set(e,e,1),this.icon.position.set(this.scene.meshMarginLeft,-q.screen.height+this.scene.meshMarginTop+e*.7,0);const t=this.scene.small?180:230,s=t;',
        'resize(){const e=this.scene.small?21:25;this.icon.scale.set(e,e,1),this.icon.position.set(this.scene.meshMarginLeft,-q.screen.height+this.scene.meshMarginTop+e*.7,0);const t=this.scene.small?225:280,s=t;'
    ),
]

FORM_A_CODE = r"""async _initAuroraWheel(){
    const TAU = Math.PI * 2;
    const CAM_YAW = -Math.PI * 0.25; // Face camera at (-13.25, 2.5, 13.25)
    const HERO_Y = 1.44;
    const root = new Gi();
    root.name = "form_a_hero_root";
    root.position.set(0, HERO_Y, 0);
    root.rotation.y = CAM_YAW;
    this.scene.add(root);
    this._auroraRoot = root;

    const oldHud = document.getElementById("aurora-wheel-hud");
    if (oldHud) oldHud.remove();

    const tTriangles = le.load("igloo/triangles_tiling.ktx2", "srgb-repeat");
    const tWind = le.load("wind_noise.ktx2", "srgb-repeat");
    const tFontMap = le.load("../fonts/IBMPlexMono-Medium-datatexture.ktx2", "data");

    // ------------------------------------------------------------------
    // A. Seamless Twilight-Slate Cloud Shadow Cushion (high contrast, zero hard box)
    // ------------------------------------------------------------------
    const backdropGeo = new kt(18.0, 9.4, 1, 1);
    const backdropMat = new fe({
        uniformsGroups: [he.UBO],
        uniforms: {
            tWind: { value: tWind },
            uReveal: { value: 1.0 }
        },
        vertexShader: `
            varying vec2 vUv;
            void main() {
                vUv = uv;
                gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
            }
        `,
        fragmentShader: `
            ${ae}
            uniform sampler2D tWind;
            uniform float uReveal;
            varying vec2 vUv;
            void main() {
                vec2 p = (vUv - vec2(0.5, 0.50)) * 2.0;
                float wind = texture2D(tWind, vUv * vec2(1.0, 0.8) + vec2(time * 0.014, 0.0)).r;
                float edgeZero = smoothstep(0.0, 0.20, vUv.x) * smoothstep(1.0, 0.80, vUv.x)
                               * smoothstep(0.0, 0.18, vUv.y) * smoothstep(1.0, 0.82, vUv.y);
                float mist = exp(-dot(p * vec2(0.76, 0.84), p * vec2(0.76, 0.84)) * 1.32) * edgeZero;
                // Deep glacial twilight slate so crisp white typography & ice-blue tags pop effortlessly over bright snow
                vec3 deepSlate = mix(vec3(0.14, 0.19, 0.29), vec3(0.20, 0.26, 0.37), wind * 0.35 + 0.25);
                float alpha = clamp(mist * 0.68, 0.0, 0.68) * uReveal;
                if (alpha < 0.004) discard;
                gl_FragColor = vec4(deepSlate, alpha);
            }
        `,
        transparent: !0,
        depthWrite: !1,
        depthTest: !1,
        side: 2
    });
    const backdropMesh = new Ce(backdropGeo, backdropMat);
    backdropMesh.position.set(0, -0.04, -1.05);
    backdropMesh.renderOrder = 965;
    root.add(backdropMesh);
    this._auroraBackdrop = backdropMesh;

    // ------------------------------------------------------------------
    // B. Subtle Polar Aurora Veil (soft luminous rim behind the upper frame)
    // ------------------------------------------------------------------
    this._auroraCurtains = [];
    [
        { w: 13.6, h: 3.8, y: 1.05, z: -1.18, alpha: 0.12, phase: 0.0, speed: 0.16, rotZ: 0.012 },
        { w: 11.8, h: 3.0, y: -1.10, z: -1.12, alpha: 0.09, phase: 2.6, speed: -0.14, rotZ: -0.012 }
    ].forEach((cfg, idx) => {
        const geom = new kt(cfg.w, cfg.h, 32, 10);
        const mat = new fe({
            uniformsGroups: [he.UBO],
            uniforms: {
                tTriangles: { value: tTriangles },
                tWind: { value: tWind },
                uAlpha: { value: cfg.alpha },
                uPhase: { value: cfg.phase },
                uSpeed: { value: cfg.speed },
                uReveal: { value: 1.0 }
            },
            vertexShader: `
                ${ae}
                uniform float uPhase;
                uniform float uSpeed;
                varying vec2 vUv;
                void main() {
                    vUv = uv;
                    vec3 pos = position;
                    float t = time * uSpeed + uPhase;
                    pos.z += sin(uv.x * 6.28318 + t) * 0.22;
                    pos.y += sin(uv.x * 3.14159) * 0.12;
                    gl_Position = projectionMatrix * modelViewMatrix * vec4(pos, 1.0);
                }
            `,
            fragmentShader: `
                ${ae}
                uniform sampler2D tTriangles;
                uniform sampler2D tWind;
                uniform float uAlpha;
                uniform float uPhase;
                uniform float uReveal;
                varying vec2 vUv;
                void main() {
                    float xMask = smoothstep(0.0, 0.28, vUv.x) * smoothstep(1.0, 0.72, vUv.x);
                    float t = time * 0.14 + uPhase;
                    float wind = texture2D(tWind, vec2(vUv.x * 1.3 - t * 0.16, vUv.y * 0.7 + t * 0.08)).r;
                    float yEnv = smoothstep(0.05, 0.45, vUv.y) * (1.0 - smoothstep(0.55, 0.98, vUv.y));
                    float rays = pow(sin(vUv.x * 16.0 + wind * 2.2 + vUv.y * 1.5) * 0.5 + 0.5, 1.8);
                    float tri = texture2D(tTriangles, vUv * vec2(4.0, 2.5) + vec2(wind * 0.03, -time * 0.04)).r;
                    vec3 col = mix(vec3(0.56, 0.76, 1.00), vec3(0.88, 0.95, 1.00), tri * 0.28 + rays * 0.30);
                    float a = xMask * yEnv * (0.40 + 0.60 * rays) * uAlpha * uReveal;
                    if (a < 0.002) discard;
                    gl_FragColor = vec4(col, a);
                }
            `,
            transparent: !0,
            depthWrite: !1,
            depthTest: !1,
            blending: pt,
            side: 2
        });
        const mesh = new Ce(geom, mat);
        mesh.position.set(0, cfg.y, cfg.z);
        mesh.rotation.z = cfg.rotZ;
        mesh.renderOrder = 968 + idx;
        root.add(mesh);
        this._auroraCurtains.push(mesh);
    });

    // ------------------------------------------------------------------
    // C. Form A Quadrant Specs — Zero-Overlap, Non-Duplicated 2x2 Matrix
    // ------------------------------------------------------------------
    const QUAD_SPECS = [
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
    ];
    this._quadSpecs = QUAD_SPECS;

    const NEXUS = [0.0, -0.30, -0.18];
    const hash1 = (n) => {
        const x = Math.sin(n * 127.1 + 311.7) * 43758.5453123;
        return x - Math.floor(x);
    };

    // ------------------------------------------------------------------
    // D. Sculpted 3-Layer Polar Particle Architecture (2,200 Crisp Particles)
    //    Wide framing halo outside the enlarged text zone so particles elevate mood without fighting copy
    // ------------------------------------------------------------------
    const P1_COUNT = 1380;
    const P2_COUNT = 112;
    const P3_COUNT = 708;
    const TOTAL_P = P1_COUNT + P2_COUNT + P3_COUNT;

    const pPos = new Float32Array(TOTAL_P * 3);
    const pTarget = new Float32Array(TOTAL_P * 3);
    const pAttrA = new Float32Array(TOTAL_P * 4);
    const pAttrB = new Float32Array(TOTAL_P * 4);

    let cursor = 0;

    for (let i = 0; i < P1_COUNT; i++) {
        const u = i / P1_COUNT;
        let x, y, z, weight;
        if (i < 980) {
            const band = i % 3;
            const theta = u * TAU * 17.0 + band * 2.094 + hash1(i * 1.9) * 0.35;
            const rx = 5.55 + band * 0.55 + (hash1(i * 2.7) - 0.5) * 1.05;
            const ry = 2.95 + band * 0.32 + (hash1(i * 3.9) - 0.5) * 0.55;
            const tilt = (band - 1) * 0.13;
            const cx = Math.cos(theta) * rx;
            const cy = Math.sin(theta) * ry;
            x = cx * Math.cos(tilt) - cy * Math.sin(tilt);
            y = -0.05 + cx * Math.sin(tilt) + cy * Math.cos(tilt);
            z = -0.72 + Math.sin(theta * 2.0 + band) * 0.55 + (hash1(i * 5.7) - 0.5) * 0.35;
            weight = 0.72;
        } else {
            const ang = hash1(i * 4.3) * TAU;
            const r = 1.2 + Math.sqrt(hash1(i * 6.1)) * 4.6;
            x = Math.cos(ang) * r;
            y = -3.05 + (hash1(i * 8.7) - 0.5) * 0.45 + Math.sin(ang * 2.0) * 0.08;
            z = -0.40 + Math.sin(ang) * r * 0.38;
            weight = 0.65;
        }

        pPos[cursor * 3] = x;
        pPos[cursor * 3 + 1] = y;
        pPos[cursor * 3 + 2] = z;

        pTarget[cursor * 3] = x * 1.4;
        pTarget[cursor * 3 + 1] = y * 1.3;
        pTarget[cursor * 3 + 2] = z + 2.4;

        pAttrA[cursor * 4] = hash1(i * 11.3);
        pAttrA[cursor * 4 + 1] = 0.35 + hash1(i * 13.7) * 0.85;
        pAttrA[cursor * 4 + 2] = hash1(i * 17.9) * TAU;
        pAttrA[cursor * 4 + 3] = 0.0;

        pAttrB[cursor * 4] = -1.0;
        pAttrB[cursor * 4 + 1] = hash1(i * 23.1) > 0.84 ? 1.0 : 0.0;
        pAttrB[cursor * 4 + 2] = x >= 0 ? 1.0 : -1.0;
        pAttrB[cursor * 4 + 3] = weight;
        cursor++;
    }

    const perQuad = Math.floor(P2_COUNT / 4);
    for (let qIdx = 0; qIdx < 4; qIdx++) {
        const q = QUAD_SPECS[qIdx];
        for (let j = 0; j < perQuad; j++) {
            const spread = (hash1(qIdx * 400 + j * 4.1) - 0.5) * 0.035;
            pPos[cursor * 3] = q.anchor[0] + spread;
            pPos[cursor * 3 + 1] = q.anchor[1] + spread;
            pPos[cursor * 3 + 2] = q.anchor[2];

            pTarget[cursor * 3] = NEXUS[0];
            pTarget[cursor * 3 + 1] = NEXUS[1];
            pTarget[cursor * 3 + 2] = NEXUS[2];

            pAttrA[cursor * 4] = j / perQuad;
            pAttrA[cursor * 4 + 1] = 0.55 + hash1(qIdx * 300 + j * 9.7) * 0.45;
            pAttrA[cursor * 4 + 2] = hash1(qIdx * 300 + j * 13.3) * TAU;
            pAttrA[cursor * 4 + 3] = 1.0;

            pAttrB[cursor * 4] = qIdx;
            pAttrB[cursor * 4 + 1] = j % 4 === 0 ? 1.0 : 0.0;
            pAttrB[cursor * 4 + 2] = q.scatter[0];
            pAttrB[cursor * 4 + 3] = 0.58;
            cursor++;
        }
    }

    for (let i = 0; i < P3_COUNT; i++) {
        const x = (hash1(i * 29.3) - 0.5) * 14.0;
        const y = (hash1(i * 31.1) - 0.5) * 6.0;
        const z = -1.4 + hash1(i * 37.7) * 2.0;
        pPos[cursor * 3] = x;
        pPos[cursor * 3 + 1] = y;
        pPos[cursor * 3 + 2] = z;

        pTarget[cursor * 3] = x * 1.5;
        pTarget[cursor * 3 + 1] = y + 1.5;
        pTarget[cursor * 3 + 2] = z + 2.6;

        pAttrA[cursor * 4] = hash1(i * 41.3);
        pAttrA[cursor * 4 + 1] = 0.25 + hash1(i * 43.9) * 0.70;
        pAttrA[cursor * 4 + 2] = hash1(i * 47.7) * TAU;
        pAttrA[cursor * 4 + 3] = 2.0;

        pAttrB[cursor * 4] = -1.0;
        pAttrB[cursor * 4 + 1] = hash1(i * 53.3) > 0.78 ? 1.0 : 0.0;
        pAttrB[cursor * 4 + 2] = x >= 0 ? 1.0 : -1.0;
        pAttrB[cursor * 4 + 3] = 0.40;
        cursor++;
    }

    const pGeo = new ot();
    pGeo.setAttribute("position", new nt(pPos, 3));
    pGeo.setAttribute("aTarget", new nt(pTarget, 3));
    pGeo.setAttribute("aAttrA", new nt(pAttrA, 4));
    pGeo.setAttribute("aAttrB", new nt(pAttrB, 4));

    const pMat = new fe({
        uniformsGroups: [he.UBO],
        uniforms: {
            uAlpha: { value: 1.0 },
            uScatter: { value: 0.0 },
            uHoverIdx: { value: -1.0 },
            uHoverBoost: { value: 0.0 },
            uMouse: { value: new b(99.0, 99.0, 0.0) },
            uDpr: { value: Math.min(window.devicePixelRatio || 1, 2) }
        },
        vertexShader: `
            ${ae}
            attribute vec3 aTarget;
            attribute vec4 aAttrA;
            attribute vec4 aAttrB;

            uniform float uAlpha;
            uniform float uScatter;
            uniform float uHoverIdx;
            uniform float uHoverBoost;
            uniform vec3 uMouse;
            uniform float uDpr;

            varying float vAlpha;
            varying float vStar;
            varying float vTemp;

            void main() {
                float seed = aAttrA.x;
                float spd = aAttrA.y;
                float phase = aAttrA.z;
                float layer = aAttrA.w;
                float quadIdx = aAttrB.x;
                float brightness = aAttrB.w;

                vec3 p = position;
                float localAlpha = brightness;
                float sizeBase = 2.0;
                vTemp = seed;

                if (layer < 0.5) {
                    float ang = time * 0.055 * (0.6 + 0.5 * spd) * (seed > 0.5 ? 1.0 : -1.0);
                    float cs = cos(ang), sn = sin(ang);
                    vec2 rotXZ = vec2(p.x * cs - (p.z + 0.5) * sn, p.x * sn + (p.z + 0.5) * cs);
                    p.x = mix(p.x, rotXZ.x, 0.25);
                    p.z = mix(p.z, rotXZ.y - 0.5, 0.25);
                    p.y += sin(time * 0.55 + phase + p.x * 0.5) * 0.07;
                    float twinkle = 0.48 + 0.52 * sin(time * 1.9 + phase * 2.0);
                    localAlpha *= twinkle * 0.80;
                    sizeBase = 1.9 + 2.6 * spd;
                } else if (layer < 1.5) {
                    float isHovered = step(abs(quadIdx - uHoverIdx), 0.25) * uHoverBoost;
                    float flowSpeed = (0.14 + 0.08 * spd) * (1.0 + isHovered * 1.15);
                    float tFlow = fract(seed + time * flowSpeed);
                    vec3 mid = (position + aTarget) * 0.5 + vec3(0.0, 0.14 * (mod(quadIdx, 2.0) < 0.5 ? 1.0 : -1.0), 0.08);
                    float inv = 1.0 - tFlow;
                    p = inv * inv * position + 2.0 * inv * tFlow * mid + tFlow * tFlow * aTarget;
                    float env = smoothstep(0.0, 0.16, tFlow) * (1.0 - smoothstep(0.82, 1.0, tFlow));
                    localAlpha = env * (0.30 + 0.58 * isHovered);
                    sizeBase = (1.8 + 1.6 * spd) * (1.0 + 0.45 * isHovered);
                    vTemp = 0.55 + 0.45 * isHovered;
                } else {
                    float rise = fract(seed + time * 0.022 * spd);
                    p.y = -2.95 + rise * 5.90;
                    p.x += sin(time * 0.34 + phase + rise * 2.8) * 0.26;
                    float env = smoothstep(0.0, 0.20, rise) * (1.0 - smoothstep(0.78, 1.0, rise));
                    float twinkle = 0.42 + 0.58 * sin(time * 2.2 + phase * 3.0);
                    // Calm dust inside the text reading zone so characters stay pristine
                    vec2 textNorm = p.xy / vec2(5.2, 2.5);
                    float calmCenter = mix(0.28, 1.0, smoothstep(0.55, 1.15, length(textNorm)));
                    localAlpha = env * twinkle * 0.48 * calmCenter;
                    sizeBase = 1.5 + 2.1 * spd;
                }

                // Magnetic mouse frost ripple
                vec2 toCursor = p.xy - uMouse.xy;
                float mDist = length(toCursor);
                float mWave = exp(-mDist * mDist * 0.85);
                vec2 pushDir = mDist > 0.001 ? toCursor / mDist : vec2(0.0, 1.0);
                p.xy += pushDir * mWave * 0.25;
                p.z += mWave * 0.24;
                localAlpha = min(0.92, localAlpha + mWave * 0.38);
                sizeBase *= (1.0 + mWave * 0.38);

                // Scroll burst & spiral scatter
                float sc = pow(clamp(uScatter, 0.0, 1.0), 1.25);
                if (sc > 0.001) {
                    vec3 burstDir = normalize(p - vec3(0.0, -0.25, -0.95) + vec3(0.001));
                    float swirl = sc * 1.55 * (0.5 + spd);
                    float cs2 = cos(swirl), sn2 = sin(swirl);
                    vec2 sw = vec2(p.x * cs2 - p.y * sn2, p.x * sn2 + p.y * cs2);
                    p.xy = mix(p.xy, sw, sc * 0.45);
                    p += burstDir * sc * (2.8 + 2.8 * spd);
                    p.z += sc * (1.8 + 2.0 * seed);
                }

                vAlpha = localAlpha * uAlpha * (1.0 - smoothstep(0.68, 1.0, uScatter));
                vStar = aAttrB.y;

                vec4 mv = modelViewMatrix * vec4(p, 1.0);
                gl_Position = projectionMatrix * mv;
                gl_PointSize = clamp(sizeBase * uDpr * (19.0 / max(-mv.z, 2.0)), 1.2, 14.0);
            }
        `,
        fragmentShader: `
            varying float vAlpha;
            varying float vStar;
            varying float vTemp;

            void main() {
                if (vAlpha < 0.005) discard;
                vec2 uv = gl_PointCoord - 0.5;
                float d = length(uv);
                if (d > 0.5) discard;

                float core = exp(-d * d * 28.0) * 0.78;
                float halo = smoothstep(0.5, 0.0, d) * 0.26;
                float crossStar = max(
                    smoothstep(0.055, 0.0, abs(uv.x)) * smoothstep(0.46, 0.0, abs(uv.y)),
                    smoothstep(0.055, 0.0, abs(uv.y)) * smoothstep(0.46, 0.0, abs(uv.x))
                ) * vStar * 0.65;

                float intensity = core + halo + crossStar;
                vec3 iceBlue = vec3(0.64, 0.82, 1.00);
                vec3 pureSnow = vec3(0.95, 0.98, 1.00);
                vec3 col = mix(iceBlue, pureSnow, clamp(core * 0.60 + vTemp * 0.40, 0.0, 1.0));
                gl_FragColor = vec4(col, clamp(intensity * vAlpha, 0.0, 0.92));
            }
        `,
        transparent: !0,
        depthWrite: !1,
        depthTest: !1,
        blending: pt
    });
    const particleField = new Fn(pGeo, pMat);
    particleField.frustumCulled = !1;
    particleField.renderOrder = 985;
    root.add(particleField);
    this._particleField = particleField;
    this._auroraMotes = particleField;

    // ------------------------------------------------------------------
    // E. Architectural Swiss Corner Ticks & Central Diamond Reticle (zero lines crossing copy)
    // ------------------------------------------------------------------
    const buildBracketGeometry = (w, h, tick = 0.20) => {
        const hw = w * 0.5, hh = h * 0.5;
        const pts = [
            -hw, hh, 0, -hw + tick, hh, 0,
            -hw, hh, 0, -hw, hh - tick, 0,
             hw, hh, 0,  hw - tick, hh, 0,
             hw, hh, 0,  hw, hh - tick, 0,
            -hw, -hh, 0, -hw + tick, -hh, 0,
            -hw, -hh, 0, -hw, -hh + tick, 0,
             hw, -hh, 0,  hw - tick, -hh, 0,
             hw, -hh, 0,  hw, -hh + tick, 0
        ];
        const g = new ot();
        g.setAttribute("position", new nt(new Float32Array(pts), 3));
        return g;
    };

    const framePts = [
        NEXUS[0], NEXUS[1] + 0.18, NEXUS[2], NEXUS[0] + 0.18, NEXUS[1], NEXUS[2],
        NEXUS[0] + 0.18, NEXUS[1], NEXUS[2], NEXUS[0], NEXUS[1] - 0.18, NEXUS[2],
        NEXUS[0], NEXUS[1] - 0.18, NEXUS[2], NEXUS[0] - 0.18, NEXUS[1], NEXUS[2],
        NEXUS[0] - 0.18, NEXUS[1], NEXUS[2], NEXUS[0], NEXUS[1] + 0.18, NEXUS[2],
        NEXUS[0] - 0.07, NEXUS[1], NEXUS[2], NEXUS[0] + 0.07, NEXUS[1], NEXUS[2],
        NEXUS[0], NEXUS[1] - 0.07, NEXUS[2], NEXUS[0], NEXUS[1] + 0.07, NEXUS[2],
        // Subtle hairline divider cleanly between quadrants (bottom ~ -1.66) and tag strip (top ~ -2.14)
        -5.30, -1.92, 0.02, -0.45, -1.92, 0.02,
         0.45, -1.92, 0.02,  5.30, -1.92, 0.02,
        -5.38, -1.92, 0.02, -5.22, -1.92, 0.02,
        -5.30, -2.00, 0.02, -5.30, -1.84, 0.02,
         5.22, -1.92, 0.02,  5.38, -1.92, 0.02,
         5.30, -2.00, 0.02,  5.30, -1.84, 0.02
    ];
    const frameGeo = new ot();
    frameGeo.setAttribute("position", new nt(new Float32Array(framePts), 3));
    const frameMat = new ga({ color: "#dce8ff", opacity: 0.34, transparent: !0, depthTest: !1, depthWrite: !1, blending: pt });
    const frameLines = new yr(frameGeo, frameMat);
    frameLines.renderOrder = 992;
    root.add(frameLines);
    this._frameLines = frameLines;

    // ------------------------------------------------------------------
    // F. Built-in MSDF Typography (`class Ui` + Optical Weight + Soft Micro-Halo)
    //    Uses `median(tMap, uv)` directly so thin CJK strokes render crisp, bold & effortless to read!
    // ------------------------------------------------------------------
    const makeMsdfText = (textStr, fontSize, colorHex, maxWidth = 14.0, weightBias = 0.042, shadowStrength = 0.58) => {
        const mesh = new Ui(
            {
                font: "IBMPlexMono-Medium",
                text: textStr,
                width: maxWidth,
                align: "center",
                lineHeight: 0.92,
                size: fontSize
            },
            {
                uniforms: {
                    tMap: { value: tFontMap },
                    uColor: { value: new Z(colorHex) },
                    uShow1: { value: 1.0 },
                    uShow2: { value: 1.0 },
                    uOpacity: { value: 1.0 },
                    uWeight: { value: weightBias },
                    uShadow: { value: shadowStrength }
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
                        // Soft optical dark polar-slate backing directly around glyph strokes (zero box artifacts)
                        float halo = smoothstep(-0.34, 0.02, sd + uWeight) * uShadow;
                        float outAlpha = max(fill, halo) * vAlpha * uOpacity;
                        if (outAlpha < 0.01) discard;
                        vec3 shadowCol = vec3(0.06, 0.09, 0.16);
                        vec3 finalCol = mix(shadowCol, uColor, fill / max(max(fill, halo), 0.001));
                        gl_FragColor = vec4(finalCol, outAlpha);
                    }
                `,
                depthWrite: !1,
                depthTest: !1,
                transparent: !0
            }
        );
        mesh.frustumCulled = !1;
        mesh.renderOrder = 1010;
        return mesh;
    };

    const readyList = [];

    // Tier 1: Commanding Identity & Positioning Header (zero overlap with corner identity)
    const headerGroup = new Gi();
    headerGroup.name = "form_a_header";
    root.add(headerGroup);

    const hKicker = makeMsdfText("////// 3年产品实战 · 需求定义 → 指标闭环", 0.255, "#CBE0FF", 14.5, 0.042, 0.62);
    hKicker.position.set(0, 2.66, 0.18);

    const hTitle = makeMsdfText("AI 产品经理 · 产品运营", 0.70, Be.colorText, 14.5, 0.052, 0.65);
    hTitle.position.set(0, 2.02, 0.24);

    const hSub = makeMsdfText("智能体系统设计  ·  用户增长运营  ·  自动化提效", 0.28, "#F2F7FF", 14.5, 0.044, 0.62);
    hSub.position.set(0, 1.36, 0.18);

    headerGroup.add(hKicker, hTitle, hSub);
    readyList.push(hKicker.ready, hTitle.ready, hSub.ready);
    this._headerGroup = headerGroup;
    this._headerMeshes = [hKicker, hTitle, hSub];

    // Tier 2: Bold 2x2 Spatial Metric Quadrants (Zero Squinting — All 4 Visible at Once)
    this._quadCards = QUAD_SPECS.map((q) => {
        const g = new Gi();
        g.name = `form_a_quad_${q.id}`;
        g.position.set(q.pos[0], q.pos[1], q.pos[2]);
        root.add(g);

        const bGeo = buildBracketGeometry(4.84, 1.32, 0.21);
        const bMat = new ga({ color: "#dce8ff", opacity: 0.42, transparent: !0, depthTest: !1, depthWrite: !1, blending: pt });
        const brackets = new yr(bGeo, bMat);
        brackets.renderOrder = 995;
        g.add(brackets);

        const fPts = new Float32Array([
            q.anchor[0], q.anchor[1], q.anchor[2],
            NEXUS[0], NEXUS[1], NEXUS[2]
        ]);
        const fGeo = new ot();
        fGeo.setAttribute("position", new nt(fPts, 3));
        const fMat = new ga({ color: "#c2d8f8", opacity: 0.22, transparent: !0, depthTest: !1, depthWrite: !1, blending: pt });
        const filament = new yr(fGeo, fMat);
        filament.renderOrder = 988;
        root.add(filament);

        const kickerMesh = makeMsdfText(q.kicker, 0.25, "#C2D8FB", 6.4, 0.042, 0.62);
        kickerMesh.position.set(0, 0.44, 0.04);

        const metricMesh = makeMsdfText(q.metric, 0.58, Be.colorText, 6.4, 0.052, 0.68);
        metricMesh.position.set(0, -0.02, 0.08);

        const proofMesh = makeMsdfText(q.proof, 0.24, "#F2F7FF", 6.6, 0.042, 0.62);
        proofMesh.position.set(0, -0.45, 0.04);

        g.add(kickerMesh, metricMesh, proofMesh);
        readyList.push(kickerMesh.ready, metricMesh.ready, proofMesh.ready);

        return {
            spec: q,
            group: g,
            brackets,
            filament,
            meshes: [kickerMesh, metricMesh, proofMesh],
            hoverVal: 0,
            pulseTimer: 0
        };
    });

    // Tier 3: Bottom Capability & Credential Strip (Zero Overlap with Quadrants)
    const tagGroup = new Gi();
    tagGroup.name = "form_a_tags";
    root.add(tagGroup);

    const tagRow1 = makeMsdfText("[ Claude Code / Cursor ]  [ Dify / n8n ]  [ RAG / MCP / Function Calling ]", 0.25, Be.colorText, 17.5, 0.044, 0.65);
    tagRow1.position.set(0, -2.26, 0.14);

    const tagRow2 = makeMsdfText("[ SQL / Python Pandas ]  [ Axure / Figma ]  [ 国一 · 软硬双高级认证 ]", 0.245, "#E8F2FF", 17.5, 0.042, 0.65);
    tagRow2.position.set(0, -2.70, 0.10);

    tagGroup.add(tagRow1, tagRow2);
    readyList.push(tagRow1.ready, tagRow2.ready);
    this._tagGroup = tagGroup;
    this._tagMeshes = [tagRow1, tagRow2];

    await Promise.all(readyList);

    this._auroraTagPlanes = this._quadCards;
    this._msdfCards = this._quadCards;
    this._activeTitle = "AI 产品经理 · 产品运营";
    this._hoveredQuad = -1;
    this._lastHoveredQuad = -1;
    this._lockHover = null;
    this._t0 = performance.now() * 0.001;
    this._localMouse = new b(99, 99, 0);
}
_updateAuroraWheel(scrollProgress = 0){
    if (!this._auroraRoot || !this._quadCards) return;
    const now = performance.now() * 0.001;
    const t = now - (this._t0 || 0);

    if (this.smoke) this.smoke.visible = !1;
    if (this.iglooOutline) this.iglooOutline.visible = !1;
    if (this.plexus) {
        if (this.plexus.container) this.plexus.container.visible = !1;
        if (this.plexus.lineMesh) this.plexus.lineMesh.visible = !1;
    }

    const intro = ie.clamp(this.introDisplacementModulator.value, 0, 1);
    const scrollFade = 1 - ie.smoothstep(0.08, 0.42, scrollProgress);
    const scrollScatter = ie.smoothstep(0.0, 0.42, scrollProgress);
    const reveal = intro * scrollFade;

    this._auroraRoot.visible = reveal > 0.004;
    if (!this._auroraRoot.visible) return;

    // Responsive scale — full 1.00 on 16:10+ desktop, cleanly fits narrower windows without clipping
    const aspect = window.innerWidth / Math.max(window.innerHeight, 1);
    const respScale = ie.clamp(aspect / 1.56, 0.50, 1.00);
    const breath = (1 + 0.004 * Math.sin(t * 0.65)) * respScale;
    this._auroraRoot.scale.setScalar(breath);

    const INV_SQRT2 = 0.70710678;
    const lx = (this.mousePosition.x * INV_SQRT2 + this.mousePosition.z * INV_SQRT2) / Math.max(respScale, 0.4);
    const ly = (this.mousePosition.y - 1.44) / Math.max(respScale, 0.4);
    this._localMouse.set(lx, ly, 0);

    const mx = ie.clamp(lx * 0.016, -0.07, 0.07);
    const my = ie.clamp(ly * 0.014, -0.05, 0.05);
    this._auroraRoot.rotation.set(-my * 0.28, -Math.PI * 0.25 + mx * 0.35, 0, "YXZ");

    let hovered = -1;
    if (this._lockHover !== null && this._lockHover !== undefined) {
        hovered = this._lockHover;
    } else if (scrollScatter < 0.05) {
        for (let i = 0; i < this._quadCards.length; i++) {
            const qp = this._quadCards[i].spec.pos;
            if (Math.abs(lx - qp[0]) < 2.42 && Math.abs(ly - qp[1]) < 0.66) {
                hovered = i;
                break;
            }
        }
    }
    if (hovered !== this._lastHoveredQuad) {
        if (hovered >= 0) {
            this._quadCards[hovered].pulseTimer = 1.0;
        }
        this._lastHoveredQuad = hovered;
    }
    this._hoveredQuad = hovered;

    const introElapsed = Math.min(t, 3.0);

    this._headerGroup.position.set(0, scrollScatter * 1.25, scrollScatter * 0.9);
    this._headerMeshes.forEach((m, idx) => {
        if (!m.material || !m.material.uniforms) return;
        const st = idx * 0.14;
        const s1 = ie.clamp((introElapsed - st) / 0.40, 0, 1) * (1.0 - scrollScatter * 1.15);
        const s2 = ie.clamp((introElapsed - st) / 0.62, 0, 1) * (1.0 - scrollScatter * 0.75);
        m.material.uniforms.uShow1.value = ie.clamp(s1, 0, 1);
        m.material.uniforms.uShow2.value = ie.clamp(s2, 0, 1);
        m.material.uniforms.uOpacity.value = reveal;
    });

    let maxHover = 0;
    this._quadCards.forEach((card, idx) => {
        const isHov = idx === hovered ? 1.0 : 0.0;
        card.hoverVal += (isHov - card.hoverVal) * 0.14;
        card.pulseTimer = Math.max(0, card.pulseTimer - 0.045);
        maxHover = Math.max(maxHover, card.hoverVal);

        const q = card.spec;
        const floatY = Math.sin(t * 0.80 + idx * 1.55) * 0.014;
        const sc = scrollScatter;
        card.group.position.set(
            q.pos[0] + q.scatter[0] * sc,
            q.pos[1] + floatY + q.scatter[1] * sc,
            q.pos[2] + card.hoverVal * 0.28 + q.scatter[2] * sc
        );
        const cardScale = 1.0 + card.hoverVal * 0.042;
        card.group.scale.setScalar(cardScale);

        const dimOthers = hovered >= 0 ? (0.58 + 0.42 * card.hoverVal) : 1.0;
        card.brackets.material.opacity = (0.38 + 0.56 * card.hoverVal) * reveal * dimOthers;
        card.filament.material.opacity = (0.16 + 0.58 * card.hoverVal) * reveal;

        card.meshes.forEach((m, lineIdx) => {
            if (!m.material || !m.material.uniforms) return;
            const st = 0.26 + idx * 0.10 + lineIdx * 0.05;
            const s1 = ie.clamp((introElapsed - st) / 0.36, 0, 1) * (1.0 - sc * 1.15);
            let s2 = ie.clamp((introElapsed - st) / 0.58, 0, 1) * (1.0 - sc * 0.85);
            if (lineIdx === 1 && card.pulseTimer > 0.01) {
                s2 = Math.min(s2, 1.0 - card.pulseTimer * 0.36);
            }
            m.material.uniforms.uShow1.value = ie.clamp(s1, 0, 1);
            m.material.uniforms.uShow2.value = ie.clamp(s2, 0, 1);
            m.material.uniforms.uOpacity.value = reveal * dimOthers;
        });
    });

    this._tagGroup.position.set(0, -scrollScatter * 1.05, scrollScatter * 0.75);
    this._tagMeshes.forEach((m, idx) => {
        if (!m.material || !m.material.uniforms) return;
        const st = 0.58 + idx * 0.12;
        const s1 = ie.clamp((introElapsed - st) / 0.42, 0, 1) * (1.0 - scrollScatter * 1.15);
        const s2 = ie.clamp((introElapsed - st) / 0.66, 0, 1) * (1.0 - scrollScatter * 0.75);
        m.material.uniforms.uShow1.value = ie.clamp(s1, 0, 1);
        m.material.uniforms.uShow2.value = ie.clamp(s2, 0, 1);
        m.material.uniforms.uOpacity.value = reveal * (hovered >= 0 ? 0.76 : 0.98);
    });

    if (this._frameLines) {
        this._frameLines.material.opacity = (0.30 + 0.18 * maxHover) * reveal;
    }
    if (this._auroraBackdrop) {
        this._auroraBackdrop.material.uniforms.uReveal.value = reveal;
    }
    this._auroraCurtains.forEach(curtain => {
        curtain.material.uniforms.uReveal.value = reveal;
    });
    if (this._particleField) {
        const u = this._particleField.material.uniforms;
        u.uAlpha.value = reveal;
        u.uScatter.value = scrollScatter;
        u.uHoverIdx.value = hovered >= 0 ? hovered : -1.0;
        u.uHoverBoost.value = maxHover;
        u.uMouse.value.set(lx, ly, 0.0);
    }
}"""


REBUILD_FONT_SH = """#!/bin/bash
# 一键重建中文字体图集（改完文案后跑这个）
# 前置: pip3 install fonttools brotly
set -euo pipefail
cd "$(dirname "$0")"
ROOT=$(pwd)

WORK=$(mktemp -d /tmp/msdf-rebuild.XXXXXX)
trap 'rm -rf "$WORK"' EXIT

echo "[1/5] 从 App3D bundle 提取全部文案中的字符..."
python3 - "$ROOT" "$WORK" <<'PYEOF'
import os, sys
root, work = sys.argv[1], sys.argv[2]
chars = set(chr(c) for c in range(0x20, 0x7F)) | set('©®´·\u2018\u2019\u201c\u201d€→↓↑←×—…')
for fn in [
    'assets/App3D-d68cb154.js',
    'assets/App3D-form-a-v6.js',
]:
    p = os.path.join(root, fn)
    if os.path.exists(p):
        s = open(p, encoding='utf-8', errors='ignore').read()
        for ch in s:
            o = ord(ch)
            if o >= 0x80 and not (0xD800 <= o <= 0xDFFF) and o < 0x10000:
                chars.add(ch)
chars_sorted = sorted(chars)
open(f'{work}/charset.txt', 'w').write('\\n'.join('0x%04X' % ord(c) for c in chars_sorted) + '\\n')
print(f'  字符总数: {len(chars_sorted)} (全量非ASCII + 可打印ASCII, 零漏字)')
PYEOF

echo "[2/5] 合并字体 (拉丁=Plex 等宽 metrics, 中文=Arial)..."
python3 tools/fonts/merge_font.py "$WORK/charset.txt" "$WORK/merged.ttf"

echo "[3/5] 生成 MSDF 图集 (size 42 / pxrange 4, 与原版一致)..."
tools/fonts/msdf-atlas-gen -font "$WORK/merged.ttf" -charset "$WORK/charset.txt" \\
  -size 42 -pxrange 4 -type msdf -format png \\
  -imageout "$WORK/atlas.png" -json "$WORK/atlas.json" | tail -2

echo "[4/5] 编码 UASTC KTX2 (必须 --lower_left_maps_to_s0t0, 否则乱码!)..."
export DYLD_LIBRARY_PATH="$ROOT/tools/ktx/lib"
tools/ktx/bin/toktx --t2 --encode uastc --uastc 4 --linear --lower_left_maps_to_s0t0 --2d \\
  "$WORK/font.ktx2" "$WORK/atlas.png"

echo "[5/5] 替换字体文件..."
cp "$WORK/atlas.json" assets/fonts/IBMPlexMono-Medium.json
cp "$WORK/font.ktx2" assets/fonts/IBMPlexMono-Medium-datatexture.ktx2

echo "完成! 浏览器 Cmd+Shift+R 强制刷新查看。"
"""


BOTTOM_LINKS_PATCH = r"""class vF{constructor(e){this.parent=e,this.ready=new Promise(t=>{this.isReady=t}),this.group=new Gi,this.group.name="texts",this.group.visible=!1,this.parent.parent.parent.scene.add(this.group),this.hintGroup=new Gi,this.hintGroup.name="copyHints",this.hintGroup.visible=!1,this.parent.parent.parent.scene.add(this.hintGroup),this._copiedTimer=null,this._isCopied=!1,this._activeIdx=0,this.init()}async init(){await Promise.all(Be.links.map((e,t)=>{const s=new Ui({font:"IBMPlexMono-Medium",text:e.title,width:10,align:"center",lineHeight:1,size:1.18,baseOffset:-.25},{uniformsGroups:[he.UBO],uniforms:{tMap:{value:le.load("../fonts/IBMPlexMono-Medium-datatexture.ktx2","data")},uColor:{value:new Z(Be.colorText)},uShow1:{value:q.devScene?1:0},uShow2:{value:q.devScene?1:0},uAlpha:{value:1},uFadePosition:{value:100},uFadeMargin:{value:100}},vertexShader:`
                    ${Nt}
                    ${Ue}

                    attribute vec3 textWeights;
                    uniform float uShow1;
                    uniform float uShow2;
                    uniform float uAlpha;

                    varying vec2 vUv;
                    varying float vAlpha;

                    void main() {
                        float tr1 = falloff(textWeights.x, 0.0, 1.0, 0.1, clamp(uShow1, 0.0, 1.0));
                        float tr2 = falloff(textWeights.x, 0.0, 1.0, 1.0, clamp(uShow2, 0.0, 1.0));

                        vUv = uv;
                        vUv.x = mod(uv.x + 0.125 * mod(floor((1.0 - tr2) * 5.753), 8.0), 1.0);
                        vAlpha = tr1 * uAlpha;

                        gl_Position = projectionMatrix * viewMatrix * billboardModelMatrix() * vec4(position, 1.0);
                    }
                `,fragmentShader:`
                        ${ii}
                        ${Ht}
                        ${Ue}
                        ${ae}

                        uniform sampler2D tMap;
                        uniform vec3 uColor;
                        uniform float uFadePosition;
                        uniform float uFadeMargin;

                        varying vec2 vUv;
                        varying float vAlpha;

                        void main() {
                            float sd = median(tMap, vUv);
                            float d = max(fwidth(sd), 0.0001);
                            float fill = smoothstep(-d, d, sd + 0.032);
                            float halo = smoothstep(-0.30, 0.02, sd + 0.032) * 0.42;
                            float alpha = max(fill, halo) * vAlpha;
                            alpha *= smoothstep(resolution.x * 0.5 + uFadePosition + uFadeMargin, resolution.x * 0.5 + uFadePosition, gl_FragCoord.x);
                            alpha *= smoothstep(resolution.x * 0.5 - uFadePosition - uFadeMargin, resolution.x * 0.5 - uFadePosition, gl_FragCoord.x);
                            if (alpha < 0.01) discard;
                            vec3 col = mix(vec3(0.08, 0.12, 0.20), uColor, fill / max(max(fill, halo), 0.001));
                            gl_FragColor = vec4(col, alpha);
                        }
                    `,depthWrite:!1,depthTest:!1});return s._textIndex=t,s.name="text",s.frustumCulled=!1,s.renderOrder=9999,this.group.add(s),s.ready})),await this.initCopyHints(),this.isReady()}async initCopyHints(){const makeHint=(text,colorHex,size)=>{const m=new Ui({font:"IBMPlexMono-Medium",text,width:28,align:"center",lineHeight:1,size,baseOffset:-.25},{uniformsGroups:[he.UBO],uniforms:{tMap:{value:le.load("../fonts/IBMPlexMono-Medium-datatexture.ktx2","data")},uColor:{value:new Z(colorHex)},uShow1:{value:q.devScene?1:0},uShow2:{value:q.devScene?1:0},uAlpha:{value:1},uFadePosition:{value:620},uFadeMargin:{value:220}},vertexShader:`${Nt}
${Ue}
attribute vec3 textWeights;uniform float uShow1;uniform float uShow2;uniform float uAlpha;varying vec2 vUv;varying float vAlpha;void main(){float tr1=falloff(textWeights.x,0.0,1.0,0.1,clamp(uShow1,0.0,1.0));float tr2=falloff(textWeights.x,0.0,1.0,1.0,clamp(uShow2,0.0,1.0));vUv=uv;vUv.x=mod(uv.x+0.125*mod(floor((1.0-tr2)*5.753),8.0),1.0);vAlpha=tr1*uAlpha;gl_Position=projectionMatrix*viewMatrix*billboardModelMatrix()*vec4(position,1.0);}`,fragmentShader:`${ii}
${Ht}
${Ue}
${ae}
uniform sampler2D tMap;uniform vec3 uColor;uniform float uFadePosition;uniform float uFadeMargin;varying vec2 vUv;varying float vAlpha;void main(){float sd=median(tMap,vUv);float d=max(fwidth(sd),0.0001);float fill=smoothstep(-d,d,sd+0.036);float halo=smoothstep(-0.34,0.02,sd+0.036)*0.55;float alpha=max(fill,halo)*vAlpha;alpha*=smoothstep(resolution.x*0.5+uFadePosition+uFadeMargin,resolution.x*0.5+uFadePosition,gl_FragCoord.x);alpha*=smoothstep(resolution.x*0.5-uFadePosition-uFadeMargin,resolution.x*0.5-uFadePosition,gl_FragCoord.x);if(alpha<0.01)discard;vec3 col=mix(vec3(0.06,0.10,0.18),uColor,fill/max(max(fill,halo),0.001));gl_FragColor=vec4(col,alpha);}`,depthWrite:!1,depthTest:!1});m.frustumCulled=!1,m.renderOrder=9999,this.hintGroup.add(m);return m.ready.then(()=>m)};this._hintItems=await Promise.all(Be.links.map(async l=>({idle:await makeHint(l.hint||l.title,"#EAF2FF",.86),active:await makeHint(l.activeHint||l.hint||l.title,"#FFFFFF",.90)}))),this.hintIdle=this._hintItems[0]?.idle,this.hintCopied=this._hintItems[0]?.active}triggerCopied(){this._copiedTimer&&clearTimeout(this._copiedTimer),this._isCopied=!0;const idx=this.parent.parent.parent.currentLink||0,pair=this._hintItems&&this._hintItems[idx],m=pair&&pair.active;m&&(re.set(m.material.uniforms.uAlpha,{value:1,overwrite:!0}),re.fromTo(m.material.uniforms.uShow1,{value:0},{value:1,duration:.35,ease:"sine.out",overwrite:!0}),re.fromTo(m.material.uniforms.uShow2,{value:0},{value:1,duration:.6,ease:"sine.out",overwrite:!0})),this._copiedTimer=setTimeout(()=>{this._isCopied=!1;const curPair=this._hintItems&&(this._hintItems[this.parent.parent.parent.currentLink||0]),h=curPair&&curPair.idle;h&&(re.set(h.material.uniforms.uAlpha,{value:1,overwrite:!0}),re.fromTo(h.material.uniforms.uShow1,{value:0},{value:1,duration:.35,ease:"sine.out",overwrite:!0}),re.fromTo(h.material.uniforms.uShow2,{value:0},{value:1,duration:.6,ease:"sine.out",overwrite:!0}))},2400)}show(e="all",t=0,s=1){this.group.visible=!0,this.group.children.forEach((n,r)=>{(e==="all"||e===r)&&(re.set(n.material.uniforms.uAlpha,{value:1,overwrite:!0}),re.fromTo(n.material.uniforms.uShow1,{value:0},{delay:t,value:1,duration:.4*s,ease:"sine.out",overwrite:!0}),re.fromTo(n.material.uniforms.uShow2,{value:0},{delay:t,value:1,duration:.75*s,ease:"sine.out",overwrite:!0}))});const idx=this.parent.parent.parent.currentLink||0,pair=this._hintItems&&this._hintItems[idx],h=pair&&pair.idle;if(!this._isCopied&&h){re.set(h.material.uniforms.uAlpha,{value:1,overwrite:!0}),re.fromTo(h.material.uniforms.uShow1,{value:0},{delay:t,value:1,duration:.4*s,ease:"sine.out",overwrite:!0}),re.fromTo(h.material.uniforms.uShow2,{value:0},{delay:t,value:1,duration:.75*s,ease:"sine.out",overwrite:!0})}}hide(e="all",t=0,s=1){this._copiedTimer&&(clearTimeout(this._copiedTimer),this._copiedTimer=null),this._isCopied=!1,this.hintGroup.visible=!1,this.group.children.forEach((n,r)=>{(e==="all"||e===r)&&(re.to(n.material.uniforms.uShow2,{delay:t,value:0,duration:.15*s,ease:"none",overwrite:!0}),re.to(n.material.uniforms.uAlpha,{delay:t*1.5,value:0,duration:.15*s,overwrite:!0,ease:"power2.out",onComplete:()=>{this.group.visible=!1}}))})}update(){Si.positionUI({camera:this.parent.parent.parent.scene.camera,mesh:this.group,x:q.screen.width*.5,y:this.parent.bottomPosition,width:25,height:25});const e=this.parent.mobile?6.8:this.parent.small?8.2:11.6,t=this.group.children.length,s=this.parent.parent.parent.currentLink,n=(s+1)%t,r=s-1<0?t-1:s-1,a=this.parent.mobile?.78:this.parent.small?.86:1.0,o=this.parent.mobile?55:this.parent.small?78:115,l=this.parent.mobile?120:this.parent.small?160:230,c=he.uniforms.resolution.value.x*o/he.uniforms.resolutionUI.value.x,h=he.uniforms.resolution.value.x*l/he.uniforms.resolutionUI.value.x;if(this._activeIdx!==s){this._activeIdx=s,this._copiedTimer&&(clearTimeout(this._copiedTimer),this._copiedTimer=null),this._isCopied=!1;const cur=this._hintItems&&this._hintItems[s];cur&&cur.idle&&(re.set(cur.idle.material.uniforms.uAlpha,{value:1,overwrite:!0}),re.fromTo(cur.idle.material.uniforms.uShow1,{value:0},{value:1,duration:.35,ease:"sine.out",overwrite:!0}),re.fromTo(cur.idle.material.uniforms.uShow2,{value:0},{value:1,duration:.55,ease:"sine.out",overwrite:!0}))}this.group.children.forEach((d,u)=>{const f=u===s||u===n||u===r;d.visible=f,d.scale.setScalar(a),u===s?d.position.set(0,0,0):u===n?d.position.set(e,0,0):u===r&&d.position.set(-e,0,0),d.material.uniforms.uFadePosition.value=c,d.material.uniforms.uFadeMargin.value=h});const p=Be.links[s],g=Boolean(this.group.visible&&p&&p.hint);if(this.hintGroup.visible=g,g&&this._hintItems){Si.positionUI({camera:this.parent.parent.parent.scene.camera,mesh:this.hintGroup,x:q.screen.width*.5,y:this.parent.bottomPosition-(this.parent.mobile?48:58),width:25,height:25});const v=he.uniforms.resolution.value.x*640/he.uniforms.resolutionUI.value.x;this._hintItems.forEach((pair,idx)=>{const isCur=idx===s;pair.idle.visible=isCur&&!this._isCopied,pair.idle.scale.setScalar(a),pair.idle.material.uniforms.uFadePosition.value=v,pair.active.visible=isCur&&this._isCopied,pair.active.scale.setScalar(a),pair.active.material.uniforms.uFadePosition.value=v})}}}class xF{constructor(e){this.parent=e,this.ready=new Promise(t=>{this.isReady=t}),this.small=!1,this.mobile=!1,this.meshMarginTop=0,this.bottomPosition=0,this.init()}async init(){const e=new kt;this.box=new Ce(e,new fe({uniforms:{tMap:{value:le.load("ui/visit-datatexture.ktx2","data")},tBlocks:{value:le.load("scroll-datatexture.ktx2","data-repeat")},uColor:{value:new Z("#ffffff")},uShow:{value:1},uRand:{value:Math.random()}},vertexShader:`
                ${Nt}

                varying vec2 vUv;
                flat varying vec2 vScale;

                void main() {
                    vUv = uv;
                    vScale = getMatrixScale(modelMatrix).xy;
                    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
                }
            `,fragmentShader:`
                ${ii}
                ${Lc}

                uniform sampler2D tMap;
                uniform sampler2D tBlocks;
                uniform vec3 uColor;
                uniform float uShow;
                uniform float uRand;

                varying vec2 vUv;
                flat varying vec2 vScale;

                vec2 hash21(float p) {
                    vec3 p3 = fract(vec3(p) * vec3(.1031, .1030, .0973));
                    p3 += dot(p3, p3.yzx + 33.33);
                    return fract((p3.xx+p3.yz)*p3.zy);
                }

                void main() {
                    vec2 uv = imagefitUV(vUv, vec2(textureSize(tMap, 0)), vScale, 1.0);
                    float a = 1.0;

                    if (uShow < 1.0) {
                        float steps = 3.0;
                        vec2 hash = hash21(floor(uShow * steps) / steps + uRand * 3.342);
                        vec2 offset = hash * 2.0 - 1.0;
                        vec2 scale = vec2(0.1, 0.15);
                        vec2 blocksUV = uv * scale + uRand * 12.4242 + offset * uRand * 4.543;
                        float blocks1 = texture2D(tBlocks, blocksUV).g * 2.0 - 1.0;
                        float displacement = 0.025;
                        uv += vec2(blocks1, 0.0) * displacement;

                        a *= sin(uShow * 30.0 + uRand * 12.4242) * 0.15 + 0.85;
                        a *= step(0.01, uShow);
                    }

                    a *= msdf(tMap, uv);
                    gl_FragColor = vec4(uColor, a);
                }
            `,depthWrite:!1,depthTest:!1,transparent:!0,blending:pt})),this.box.name="box",this.box.frustumCulled=!1,this.box.renderOrder=999,this.box.visible=!1,this.parent.parent.scene.add(this.box),this.hitPlane=new Ce(new kt,new fe({uniforms:{},vertexShader:"void main(){gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0);}",fragmentShader:"void main(){discard;}",transparent:!0,depthWrite:!1,depthTest:!1})),this.hitPlane.frustumCulled=!1,this.hitPlane.visible=!1,this.parent.parent.scene.add(this.hitPlane),this.interaction=new Er({meshes:[this.box,this.hitPlane],camera:this.parent.parent.scene.camera,hoverCursor:!0,onHover:t=>{t.action==="hover_in"&&(this.show(.75,!0),Q.emit("webgl_play_audio","ui-long"))},onClick:t=>{this.triggerAction()}}),this.texts=new vF(this),await this.texts.ready,this.isReady()}triggerAction(){Q.emit("webgl_ui_particles_clicked");const r=Be.links[this.parent.parent.currentLink];if(r&&r.copyText){this.copyAndNotify(r)}else if(r&&r.url){const w=window.open(r.url,"_blank");if(w){try{w.opener=null}catch(e){}w.focus&&w.focus()}else{const a=document.createElement("a");a.href=r.url,a.target="_blank",a.rel="noopener",document.body.appendChild(a),a.click(),a.remove()}Q.emit("webgl_play_audio","ui-long"),this.texts&&this.texts.triggerCopied&&this.texts.triggerCopied()}}copyAndNotify(e){const t=String(e.copyText||"");if(t){if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).catch(()=>{})}else{const s=document.createElement("textarea");s.value=t,s.style.cssText="position:fixed;opacity:0;pointer-events:none;",document.body.appendChild(s),s.select();try{document.execCommand("copy")}catch(n){}s.remove()}}Q.emit("webgl_play_audio","ui-long"),this.texts&&this.texts.triggerCopied&&this.texts.triggerCopied()}show(e=1,t=!1,s=!0){var r;s&&(this.box.visible=!0,this.box.material.uniforms.uRand.value=Math.random(),re.fromTo(this.box.material.uniforms.uShow,{value:0},{value:1,duration:.3*e,ease:"none",overwrite:!0})),this.interaction.enable();const n=t?this.parent.parent.currentLink:"all";(r=this.texts)==null||r.show(n,0,n!=="all"?.7:1)}hide(){var e;re.fromTo(this.box.material.uniforms.uShow,{value:1},{value:0,duration:.15,ease:"power2.out",overwrite:!0,onComplete:()=>{this.box.visible=!1}}),this.interaction.disable(),(e=this.texts)==null||e.hide("all")}update(){var s;this.small=q.screen.width<Be.breakpointW||q.screen.height<Be.breakpointH,this.mobile=q.screen.width<Be.breakPointMobile||q.screen.height<Be.breakPointMobile,this.meshMarginTop=this.mobile?Be.topMarginMobile:this.small?Be.topMarginLow:Be.topMargin,this.bottomPosition=q.screen.height-this.meshMarginTop-(this.mobile?88:34);const e=this.mobile?185:this.small?225:270,t=e/3.125;Si.positionUI({camera:this.parent.parent.scene.camera,mesh:this.box,x:q.screen.width*.5,y:this.bottomPosition,width:e,height:t}),Si.positionUI({camera:this.parent.parent.scene.camera,mesh:this.hitPlane,x:q.screen.width*.5,y:this.bottomPosition-(this.mobile?22:28),width:this.mobile?280:380,height:this.mobile?104:120}),(s=this.texts)==null||s.update()}}class yF{constructor(e){this.parent=e,this.ready=new Promise(t=>{this.isReady=t}),this.group=new Gi,this.group.name="ui",this.parent.mesh.add(this.group),this.preventChangeLink=!1,this.enabled=!1,this.init()}async init(){await Promise.all([this.createArrows(),this.createBottomLink()]),Q.on("webgl_ui_particles_clicked",this.onUIClicked,this),Q.on("touch_click",this.onClick,this),Q.on("touch_end",this.onTouchEnd,this),Q.on("keydown",this.onKeyDown,this),this.isReady()}createArrows(){return this.arrows=new gF(this),this.arrows.ready}createBottomLink(){return this.bottom=new xF(this),this.bottom.ready}onUIClicked(e){this.preventChangeLink=!0,Promise.resolve().then(()=>Promise.resolve()).then(()=>{this.preventChangeLink=!1})}onClick(e){if(!this.enabled)return;if(Math.abs(e.position11.x)<.24&&Math.abs(e.position11.y)<.45){this.bottom&&this.bottom.triggerAction();return}this.changeLink(e.position11.x<0?-1:1)}onTouchEnd(e){this.enabled&&Math.abs(e.dragged.x)>100&&Math.abs(e.swipeVelocity.x)>1e3&&this.changeLink(e.dragged.x<0?-1:1)}onKeyDown(e){this.enabled&&(e.key==="ArrowRight"?this.changeLink(1):e.key==="ArrowLeft"&&this.changeLink(-1))}changeLink(e=1){Promise.resolve().then(()=>{var s,n;if(this.preventChangeLink)return;e===-1?this.parent.currentLink=this.parent.currentLink===0?this.parent.vdbs.length-1:this.parent.currentLink-1:this.parent.currentLink=(this.parent.currentLink+1)%this.parent.vdbs.length,re.fromTo(this.parent.mesh.computationMaterial.uniforms.uAdditionalNoise,{value:1},{value:0,duration:.5,ease:"power2.inOut",overwrite:!0}),this.parent.mesh.computationMaterial.uniforms.tVolume.value=this.parent.vdbs[this.parent.currentLink],this.parent.mesh.computationMaterial.uniforms.uVolumeScale.value=this.parent.vdbScales[this.parent.currentLink],this.parent.mesh.computationMaterial.uniforms.uRotation.value=Math.PI*1.5,(s=this.arrows)==null||s.show(e===1?"right":"left",.75),(n=this.bottom)==null||n.show(1,!1,!1),Q.emit("webgl_play_audio","ui-long");const t=this.parent.scene.floor.additionalTime+4*-e;re.to(this.parent.scene.floor,{additionalTime:t,duration:3,ease:"power4.out",overwrite:!0}),this.parent.soundControl.splatTargetVelocity+=1})}update(){if(this.parent){if(!q.devScene){const e=this.parent.scene.progress;e>.64&&e<.9?this.enable():this.disable()}[this.arrows,this.bottom].forEach(e=>e==null?void 0:e.update())}}enable(){var e,t;this.enabled||(this.enabled=!0,(e=this.arrows)==null||e.show(),(t=this.bottom)==null||t.show(),Q.emit("webgl_play_audio","ui-long"))}disable(){var e,t;this.enabled&&(this.enabled=!1,this.preventChangeLink=!1,(e=this.arrows)==null||e.hide(),(t=this.bottom)==null||t.hide(),this.parent.scene.progress<this.parent.scene.finalScrollAutocenter&&Q.emit("webgl_play_audio","ui-long"))}}class _F{constructor(e){this.parent=e,this.init()}init(){const e=new GA(.27,0);this.mesh=new Ce(e,new qy),this.mesh.position.set(0,-9.785,0),this.mesh.updateMatrixWorld(),this.interaction=new Er({camera:this.parent.scene.camera,meshes:[this.mesh],onMove:this.onMouseMove,onHover:this.onMouseHover,ctx:this}),this.splatPosition=new b,this.splatLastPosition=new b,this.splatLastMoveTime=0,this.splatLastRenderTime=0,this.splatTargetVelocity=0,this.splatVelocity=0,this.splatHovered=!1}onMouseMove(e){const t=e.interactions[0];t&&this.splatPosition.copy(t.point)}onMouseHover(e){this.splatHovered=!0}update(e=0){if(e>0?this.interaction.enable():this.interaction.disable(),Fe.time-this.splatLastRenderTime<.015)return;this.splatLastRenderTime=Fe.time;let t=this.splatPosition.distanceTo(this.splatLastPosition);const s=Fe.time-this.splatLastMoveTime;t>0&&(this.splatLastMoveTime=Fe.time),(s>.15||this.splatHovered||t>.3)&&(this.splatLastPosition.copy(this.splatPosition),t=0),this.splatHovered=!1,this.splatTargetVelocity+=t*4,this.splatTargetVelocity*=.97,this.splatTargetVelocity=ie.clamp(this.splatTargetVelocity,0,e),this.splatVelocity=ie.lerp(this.splatVelocity,this.splatTargetVelocity,.05),this.splatVelocity=ie.clamp(this.splatVelocity,0,e),this.splatLastPosition.copy(this.splatPosition),this.parent.scene._particlesVolume=.04*e+this.splatVelocity*.21}}"""




def sub1(text, before, after):
    assert before in text, f"missing anchor: {before[:80]!r}"
    return text.replace(before, after, 1)


def main():
    app = (ROOT / "assets/App3D-d68cb154.js").read_text(encoding="utf-8")
    for before, after in [GROUND_UNIFORM_ADD, GROUND_DECL_ADD, GROUND_COLOR_ADD, U3_FRAG_HIDE, OUTLINE_HIDE, *COPY_REPLACEMENTS]:
        app = sub1(app, before, after)

    raw_msdf_frag = "alpha *= msdf(tMap, uv);\n                        gl_FragColor = vec4(uColor, alpha);"
    crisp_msdf_frag = "float sd = median(tMap, uv); float d = max(fwidth(sd), 0.0001); alpha *= smoothstep(-d, d, sd + 0.032);\n                        gl_FragColor = vec4(uColor, alpha);"
    assert app.count(raw_msdf_frag) >= 3
    app = app.replace(raw_msdf_frag, crisp_msdf_frag)
    raw_msdf_frag2 = "alpha *= msdf(tMap, uv);\n                    gl_FragColor = vec4(uColor, alpha);"
    crisp_msdf_frag2 = "float sd = median(tMap, uv); float d = max(fwidth(sd), 0.0001); alpha *= smoothstep(-d, d, sd + 0.032);\n                    gl_FragColor = vec4(uColor, alpha);"
    assert app.count(raw_msdf_frag2) >= 2
    app = app.replace(raw_msdf_frag2, crisp_msdf_frag2)

    vf_start = app.find("class vF{")
    wf_start = app.find("class wF{")
    assert vf_start != -1 and wf_start != -1 and wf_start > vf_start
    app = app[:vf_start] + BOTTOM_LINKS_PATCH + app[wf_start:]

    init_anchor = "this.plexus=new R3({scene:this.scene,parent:this}),await this.plexus.ready,this.scene.add(this.mesh),this.isReady()}"
    init_replace = "this.plexus=new R3({scene:this.scene,parent:this}),await this.plexus.ready,this.scene.add(this.mesh),await this._initAuroraWheel(),this.isReady()}\n" + FORM_A_CODE
    app = sub1(app, init_anchor, init_replace)

    assert "./index-2e130bc1.js" in app
    app = app.replace("./index-2e130bc1.js", "./index-form-a-v6.js")
    (ROOT / "assets/App3D-form-a-v6.js").write_text(app, encoding="utf-8")

    idx_js = (ROOT / "assets/index-2e130bc1.js").read_text(encoding="utf-8")
    assert "App3D-d68cb154.js" in idx_js
    (ROOT / "assets/index-form-a-v6.js").write_text(idx_js.replace("App3D-d68cb154.js", "App3D-form-a-v6.js"), encoding="utf-8")

    html = (ROOT / "index.html").read_text(encoding="utf-8")
    if not (ROOT / "index.html.prod.bak").exists():
        (ROOT / "index.html.prod.bak").write_text(html, encoding="utf-8")
    assert "index-2e130bc1.js" in html or "index-form-a-v6.js" in html
    (ROOT / "index.html").write_text(html.replace("index-2e130bc1.js", "index-form-a-v6.js"), encoding="utf-8")
    (ROOT / "rebuild_font.sh").write_text(REBUILD_FONT_SH, encoding="utf-8")
    print("Successfully built production App3D-form-a-v6.js + index-form-a-v6.js + index.html in igloo-clone")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
