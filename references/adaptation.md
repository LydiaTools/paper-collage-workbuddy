# 相对 Vox Director 的改造

基线为 Alisa0808/vox-director，提交 6a85a7c341610442a6a5b1885e6e0217ab82a11f。

|环节|继承|本版本改动|
|---|---|---|
|故事与分镜|叙事弧、beat/shot结构、景别、运镜与元素动作分开规划|增加生活职场受众问题与实际动作结果；镜头数量按故事和真实音轨安排|
|风格与素材|prompt-guide和beat-layer原资料；styles.py的风格组合代码直接复用|用WorkBuddy实际模型组织输入；橙绿奶油白；文字独立成层、素材不烧标题|
|执行后端|分阶段组织项目与交付|默认WorkBuddy自身模型与本地渲染；不强依赖Atlas Cloud API|
|动画|分层纸片、镜头运动与物件运动两条轴|HyperFrames/GSAP，稳定纹理与标题，动作完成停稳，60fps；保留已认可人物样片模块，并允许新故事创建自己的HTML工程|
|声音|旁白与配乐分开、音乐在人声下让路|本地原创器乐；保留用户指定剪映原生音轨；过长旁白拒绝静默截断|
|合成和交付|画面、声音、字幕与成片的阶段化处理|最终带音轨MP4、分镜、提示词、动作表、HTML、素材、配乐与运行报告一并交付|

## 直接继承的文件

- scripts/upstream_styles.py ← 上游 scripts/styles.py，原内容保留，workflow.py实际调用 compose_collage_prompt 与 resolve_theme。
- references/upstream/beat-layer.md ← 上游同名文件，作为故事层资料。
- references/upstream/prompt-guide.md ← 上游同名文件，作为视觉层资料。
- LICENSE.upstream ← 上游 MIT 许可。

上述文件实际摘要见 upstream-origin.json。它们为保留的上游原资料，旧模型清单、外部链接与研究性说法不作为本版本已实调或已验证能力；执行规则以根 SKILL.md 为准。

## 能力边界

这是一套给执行助手使用的完整制作 Skill，不是一个只调用脚本就能凭空造出任何故事全部素材的模型。随包三段人物样片已经接通；任意新选题需要 WorkBuddy 实际组织新分镜、准备素材并制作对应 HTML 动作。本版本没有接入 MiniMax-H3、Veo、Atlas Cloud，也不以来源署名代替我们自己的交付入口。
