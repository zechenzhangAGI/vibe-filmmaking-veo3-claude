# Veo 3.1 Generation Prompts - Orchestra Launch Video

## Generation Strategy

Based on Veo 3.1 capabilities:
- **Max duration:** 8 seconds per clip
- **Direct generation:** Text-to-video without keyframes (simpler workflow)
- **Extension:** Use for connected narrative scenes
- **Independent:** Generate separately for distinct moments

### Clip Plan:

| Clip | Time | Duration | Type | Notes |
|------|------|----------|------|-------|
| **1. Galileo** | 0-5s | 5s | Independent | Opening shot, standalone |
| **2. Time Collapse** | 5-10s | 5s | Extend from #1 | Connected transition |
| **3A-3F. Hell Montage** | 10-15s | 6x1s | Independent each | Rapid cuts, generate separately |
| **4. Breaking Point** | 15-18s | 3s | Independent | Distinct emotional beat |
| **5. Light Returns** | 18-22s | 4s | Extend from #4 | Same person, narrative continuation |
| **6. Discovery Abstract** | 22-28s | 6s | Independent | Abstract visuals, distinct style |
| **7. Constellation** | 28-33s | 5s | Extend from #6 | Pull back reveal |

**Total:** 8 primary clips (montage = 6 mini clips)

---

## Veo 3.1 Prompt Structure

Following Google's best practices, each prompt includes:
1. **Subject** - What/who
2. **Action** - What's happening
3. **Setting** - Where/when
4. **Style** - Visual aesthetic
5. **Camera** - Movement, angle, lens
6. **Composition** - Framing, depth of field
7. **Lighting** - Ambiance, mood
8. **Audio** (optional) - Sound cues

---

## CLIP 1: Galileo's Wonder (0-5s)
**Type:** Independent generation
**Duration:** 5 seconds
**Model:** `veo-3.1-generate-preview`

### Veo Prompt:
```
Galileo Galilei stands at a brass telescope gazing upward at infinite starry night sky in 1610 Tuscany. Wide cinematic establishing shot emphasizing dramatic scale of cosmos above and single human figure below. Period-accurate Renaissance clothing, doublet and robe. Warm golden candlelight from nearby stone villa window illuminates his figure from side, mixing with cool blue starlight from above. His face shows pure wonder and awe looking upward at the heavens. Open Tuscan landscape with rolling hills barely visible in darkness. Camera is static wide shot, allowing the moment to breathe. Shot on 35mm film with warm color grading, Terrence Malick aesthetic. Shallow depth of field with stars in sharp focus and foreground slightly soft. Intimate spiritual moment of discovery between one man and infinite universe. Sense of pure curiosity unencumbered. Renaissance period accuracy in costume and telescope design. Contemplative and serene mood. Audio: soft night wind through Italian countryside, distant cricket chirps, quiet telescope brass adjustment, gentle breath of wonder.
```

### Key Elements:
- **Subject:** Galileo Galilei at telescope
- **Action:** Gazing upward at stars in wonder
- **Setting:** 1610 Tuscany, night, open landscape
- **Style:** Terrence Malick aesthetic, 35mm film, Renaissance period accurate
- **Camera:** Static wide shot, shallow depth of field
- **Lighting:** Warm candlelight + cool starlight mixing
- **Mood:** Spiritual, pure wonder, contemplative
- **Audio:** Night wind, crickets, telescope adjustment, breath

### Technical Settings:
```python
{
    "model": "veo-3.1-generate-preview",
    "duration": 5,
    "resolution": "1080p",
    "aspect_ratio": "16:9",
    "frame_rate": 24
}
```

---

## CLIP 2: Time Collapses (5-10s)
**Type:** Extend from Clip 1
**Duration:** 5 seconds
**Model:** `veo-3.1-generate-preview`

### Veo Prompt:
```
Cinematic time-lapse transformation from same telescope position. The starry night sky rapidly cycles through day and night multiple times creating streaking star trails and sun arcs. The humble brass telescope morphs and transforms into modern institutional observatory equipment with chrome and digital displays. Single warm candlelight multiplies into harsh fluorescent ceiling grid lights. The open Tuscan landscape becomes enclosed by sterile institutional walls and doors appearing around the scene. The solitary figure of Galileo becomes crowded by multiple modern researchers in contemporary clothing and lab coats. Camera maintains same wide framing throughout transformation. Color temperature shifts dramatically from warm golden candlelight tones to cold blue-gray fluorescent institutional lighting. Sense of science becoming industrialized, systematized, and losing intimacy with discovery. Time compression effect with motion blur and temporal layers visible. Shot on 35mm film transitioning to digital aesthetic. Audio: time compression whoosh sound, wind accelerating, institutional sounds building (fluorescent buzz, electronic hums, door mechanisms, keyboard clicks), renaissance lute music distorting and becoming dissonant.
```

### Key Elements:
- **Subject:** Same telescope scene transforming through time
- **Action:** Time-lapse metamorphosis from 1610 to 2025
- **Setting:** Same position, changing from open landscape to institutional lab
- **Style:** Temporal transformation, 35mm to digital
- **Camera:** Static wide framing maintained throughout
- **Lighting:** Warm candlelight → cold fluorescent transformation
- **Mood:** Loss of intimacy, industrialization of science
- **Audio:** Time whoosh, accelerating sounds, music distorting

### Technical Settings:
```python
{
    "model": "veo-3.1-generate-preview",
    "duration": 5,
    "resolution": "1080p",
    "aspect_ratio": "16:9",
    "frame_rate": 24,
    "extend_from": "clip_1_video_id"  # Extension parameter
}
```

---

## CLIP 3A: Terminal Errors (10-11s)
**Type:** Independent generation
**Duration:** 1 second
**Model:** `veo-3.1-fast-preview` (faster for short cuts)

### Veo Prompt:
```
Extreme close-up macro shot of computer terminal screen showing Python error messages rapidly scrolling upward in red text on black background. Text clearly shows "ModuleNotFoundError: No module named 'torch'", "CUDA installation not found", "RuntimeError: dependency conflict detected". Realistic developer terminal interface with monospace font. Screen has subtle grain and flicker effect like real CRT or LCD monitor. Cold blue screen glow. Text scrolls rapidly creating sense of cascading failures. Camera is static extreme close-up filling frame with terminal window. Harsh overhead fluorescent lighting reflecting on screen glass. Dark moody institutional atmosphere. Technical frustration visible in rapid scrolling. Shot with digital camera, clinical framing, high contrast. Audio: rapid error beeps, system alert tones, keyboard key mashing sounds, computer fan running loudly, frustrated exhale from user off-screen.
```

### Key Elements:
- **Subject:** Computer terminal with error messages
- **Action:** Errors scrolling rapidly upward
- **Setting:** Close-up on screen, institutional office
- **Style:** Clinical digital, realistic dev environment
- **Camera:** Static extreme close-up macro
- **Lighting:** Cold blue screen glow + fluorescent reflection
- **Mood:** Technical frustration, cascading failures
- **Audio:** Error beeps, keyboard mashing, fan, exhale

---

## CLIP 3B: Literature Overwhelm (11-12s)
**Type:** Independent generation
**Duration:** 1 second

### Veo Prompt:
```
Close-up shot of person's hands frantically scrolling through academic PDF research paper on laptop trackpad. Browser shows 47 tabs open at top of screen, all research papers with dense titles visible. PDF on screen shows dense text, equations, and scientific figures. Hands show agitated scrolling motion, finger swiping rapidly. Warm desk lamp illuminates hands from side creating dramatic shadows. Laptop keyboard visible in foreground slightly out of focus. Person's body language suggests overwhelm and information overload. Shot from 45-degree angle overhead focusing on hands and screen. Documentary style, natural realistic lighting. Sense of drowning in academic literature and unable to find what's needed. Shot on digital camera with shallow depth of field focusing on scrolling hand. Audio: rapid mouse trackpad scrolling clicks, page scroll sounds, frustrated breathing, papers rustling on desk nearby, desk lamp electrical hum.
```

---

## CLIP 3C: GPU Queue Wait (12-13s)
**Type:** Independent generation
**Duration:** 1 second

### Veo Prompt:
```
Close-up shot of laptop screen displaying institutional compute cluster queue management interface. Screen shows large prominent text: "GPU Queue Status: Position 89 of 156 | Estimated wait time: 14h 23m" in institutional blue and gray web design. Realistic university computing portal interface with tables and status indicators. Cursor is visible clicking refresh button showing number not changing. Harsh fluorescent office lighting reflects on laptop screen glass creating slight glare. Cold impersonal sterile color palette of blues and grays. Screen interface has bureaucratic design with many fields and checkboxes. Camera static straight-on at screen filling frame. Shot with digital camera, clinical composition. Sense of endless waiting in digital purgatory. Audio: single mouse click sound, fluorescent light buzzing overhead, computer fan humming, keyboard tap, frustrated exhale, quiet institutional office ambiance, clock ticking in background.
```

---

## CLIP 3D: Environment Hell (13-14s)
**Type:** Independent generation
**Duration:** 1 second

### Veo Prompt:
```
Extreme close-up of hands rapidly typing terminal commands for environment setup. Screen visible showing terminal with commands: "pip install tensorflow", "conda create --name myenv", immediately followed by error messages in red text. Multiple overlapping terminal windows visible on screen showing configuration attempts. Hands show frustration in typing rhythm, hitting keys harder. Cold laptop screen glow illuminates hands from below. Keyboard is modern MacBook style with backlighting. Camera angle from side showing both hands typing and screen reflection. Shot with shallow depth of field focusing on hands in motion. Sense of sisyphean technical infrastructure task. Digital camera aesthetic, realistic developer environment. Audio: rapid keyboard typing sounds with aggressive key strikes, error notification beeps, computer fan accelerating, frustrated grunt from person, multiple terminal bells dinging, desk surface vibration from hard typing.
```

---

## CLIP 3E: Permission Denied (14-15s)
**Type:** Independent generation
**Duration:** 1 second

### Veo Prompt:
```
Close-up shot of laptop screen showing email inbox with multiple rejection emails visible. Subject lines clearly readable: "Grant Application Status: DENIED", "Access Request: Insufficient Credentials", "Application Declined", "Under Review - Day 287 of 365". Email interface is realistic institutional design. Cursor scrolls slowly through inbox showing repeated rejections. Cold fluorescent office lighting reflects on screen. Person's face partially visible in reflection on dark areas of screen showing disappointment. Screen has realistic email client interface with folder navigation and preview pane. Camera static straight-on at laptop screen. Shot with digital camera, documentary realism. Sense of bureaucratic barriers and repeated institutional rejection. Audio: single email notification "ding" sound (disappointing tone), mouse scroll wheel clicking, quiet office ambiance, disappointed sigh from person, fluorescent light buzz, keyboard spacebar tap.
```

---

## CLIP 3F: Buried in Papers (15-16s)
**Type:** Independent generation
**Duration:** 1 second

### Veo Prompt:
```
Medium-wide shot of researcher sitting at desk completely obscured behind impossibly tall stacks of academic papers and printed journal articles. Only top of person's head barely visible behind paper towers. Multiple stacks of varying heights create complex layered composition. Papers have visible academic formatting with graphs, equations, and dense text on edges. Dramatic side lighting from window creates strong shadows and highlights on paper edges. Sterile institutional office environment. Person's overwhelmed posture visible through papers. Stacks are precarious and overwhelming in quantity. Camera static medium-wide framing emphasizing scale of paper mountains. Shot with cinematic digital camera, dramatic composition. Kafkaesque sense of being buried and isolated by information overload. Audio: papers rustling heavily, stack being moved causing paper avalanche sound, heavy overwhelmed sigh from person, papers sliding and shifting, muffled room ambiance behind papers, oppressive silence underneath paper sounds.
```

---

## CLIP 4: Breaking Point (15-18s)
**Type:** Independent generation
**Duration:** 3 seconds

### Veo Prompt:
```
Close-up cinematic portrait of exhausted researcher sitting back in office chair with defeated posture. Person stops all activity and slowly sits back. Camera angle from slightly below looking up shows person's face and institutional fluorescent ceiling grid visible above. Person looks down at their own hands resting in lap showing resignation. Eyes show deep fatigue with dark circles visible. Institutional office environment with fluorescent lights creating harsh overhead shadows on face. Person slowly closes eyes and takes one deep breath visible in chest movement. Camera is static close framing, allowing emotional beat to breathe. After breath, cut to pure black screen for final second. Shot on cinematic digital camera with dramatic low-key lighting. Rembrandt lighting quality with strong contrast. Intimate moment of defeat and giving up. Sense of soul crushed by system. Audio: all environmental sounds fade out during shot, just person's heavy tired breathing clearly audible, then single slow heartbeat sound, then complete silence as screen goes black, hold uncomfortable silence.
```

### Key Elements:
- **Subject:** Exhausted researcher, defeated
- **Action:** Stops, sits back, looks down, closes eyes, breathes
- **Setting:** Institutional office, harsh lighting
- **Style:** Cinematic portrait, Rembrandt lighting, dramatic
- **Camera:** Static close-up from below, emotional framing
- **Lighting:** Harsh fluorescent overhead creating shadows
- **Mood:** Defeat, resignation, rock bottom, giving up
- **Audio:** Breathing fades in, single heartbeat, then complete silence

---

## CLIP 5: Light Returns (18-22s)
**Type:** Extend from Clip 4 (same person, narrative continuation)
**Duration:** 4 seconds

### Veo Prompt:
```
Continue from previous shot of same person in darkness. Person remains with eyes closed in dark frame. Warm golden amber light slowly begins to glow and intensify from bottom of frame, coming from laptop screen below camera (off-screen). Light gradually illuminates person's face from beneath creating dramatic chiaroscuro effect and spiritual quality. Color temperature shifts from cold to warm as light grows. Person's closed eyes visible in growing warm light. Eyes slowly begin to open showing transformation in expression from exhaustion to curiosity. Subtle shift visible in facial expression - tension releases slightly. Dramatic Caravaggio-style lighting with strong contrast between darkness and warm light. Light has golden amber quality, inviting and hopeful not cold blue. Camera remains static allowing transformation to happen naturally through lighting change. Shot with cinematic camera capturing subtle performance. Intimate portrait of hope emerging and transformation beginning. Shallow depth of field focused on face. Audio: soft warm electronic hum begins (inviting not cold), person's breathing becomes lighter and more hopeful, single pure clear piano note rings out, ambient warm string pad begins to swell underneath, sense of darkness lifting.
```

### Key Elements:
- **Subject:** Same person from previous clip
- **Action:** Light grows, eyes open, expression transforms
- **Setting:** Same position, darkness to light
- **Style:** Caravaggio chiaroscuro, spiritual awakening
- **Camera:** Static, same framing, light transformation
- **Lighting:** Darkness → warm golden amber from below
- **Mood:** Hope emerging, transformation, rebirth
- **Audio:** Warm electronic hum, lighter breathing, piano note, strings

---

## CLIP 6: Discovery Abstract (22-28s)
**Type:** Independent generation
**Duration:** 6 seconds

### Veo Prompt:
```
Abstract artistic sequence showing discovery and creation visualized through organic metaphors. Macro photography of black ink dispersing in clear water creating beautiful fractal patterns and organic forms. Transition to abstract neural network visualization with golden synapses lighting up in deep blue space, nodes connecting in organic pattern forming network. Mathematical equations and formulas appearing in space like chalk on blackboard, connecting with elegant lines. Luminous data flows like glowing rivers of particles streaming through space. White light refracts through crystal prism creating rainbow spectrum with visible light rays. All visuals use warm color palette of blue (#0099FF Orchestra brand) and amber gold tones, never cold. Fast-paced but organic motion, alive and beautiful not mechanical. High-speed macro photography mixed with elegant data visualization. Scientific beauty and wonder captured visually. No product UI shown, pure abstract representation of discovery and understanding emerging. Shot with macro lenses and motion graphics, cinematic quality throughout. Sense of ideas spreading naturally, intelligence emerging, understanding building. Audio: warm electronic ambient soundscape, strings building with hopeful restrained emotion, organic sounds mixed with digital (water, light harmonics, gentle electronic pulses), human and AI synthesis in sound, building but never bombastic.
```

### Key Elements:
- **Subject:** Abstract visualizations of discovery
- **Action:** Ink dispersing, networks forming, equations connecting, data flowing, light refracting
- **Setting:** Abstract space, macro and data viz
- **Style:** Scientific beauty, organic metaphors, Orchestra colors
- **Camera:** Macro close-ups, motion graphics camera moves
- **Lighting:** Warm blue and amber, never cold tech
- **Mood:** Creation, organic intelligence, beautiful discovery
- **Audio:** Warm electronic, strings, organic + digital synthesis

---

## CLIP 7: Constellation (28-33s)
**Type:** Extend from Clip 6 (pull back reveal)
**Duration:** 5 seconds

### Veo Prompt:
```
Camera pulls back from abstract visualizations revealing concrete reality. Original researcher from earlier clips now visible working at laptop in warm screen glow. Camera continues smooth pullback revealing wider dark space. Other diverse people gradually appear throughout dark environment around the first person. Each person has their own warm laptop/screen glow creating points of light in darkness. Different ages visible: teenager on bed, elderly person at kitchen table, parent in home office, young adult in cafe. Different settings: bedroom, kitchen, modest apartment, small cafe. Each person working, discovering, creating on their own device. Warm golden amber screen glows create constellation pattern of lights scattered through dark space like stars. Aerial perspective slowly revealing global community connected by curiosity not institutions. Wide cinematic framing showing multiple people simultaneously. Each warm glow is island of light in dark sea. Documentary realism mixed with poetic staging for visual impact. Shot with cinematic camera on smooth dolly pullback. Sense of movement forming, not alone, global democratization visible. Audio: multiple keyboards typing in gentle rhythm (almost musical not chaotic), warm strings swell with emotion but remain restrained, sense of collective breathing and shared purpose, building toward manifesto moment, hope and connection audible.
```

### Key Elements:
- **Subject:** Multiple diverse people with laptops
- **Action:** Camera pulls back revealing constellation
- **Setting:** Various locations in darkness, global
- **Style:** Documentary realism + poetic staging, aerial view
- **Camera:** Smooth dolly pullback, wide framing
- **Lighting:** Multiple warm screen glows creating constellation
- **Mood:** Community, connection, movement, democratization
- **Audio:** Multiple keyboards (musical), strings swell, collective breathing

---

## Production Notes

### Generation Order:
1. **Generate Clip 1** (Galileo) - foundation scene
2. **Extend to Clip 2** (Time Collapse) - connected narrative
3. **Generate Clips 3A-3F** (Montage) - independently, can run parallel
4. **Generate Clip 4** (Breaking Point) - distinct emotional beat
5. **Extend to Clip 5** (Light Returns) - same person continuation
6. **Generate Clip 6** (Discovery Abstract) - distinct visual style
7. **Extend to Clip 7** (Constellation) - pull back reveal

### Rate Limiting Strategy:
- Wait 30-60 seconds between generation requests
- Generate montage clips (3A-3F) with 30s intervals
- Extensions may need longer wait time

### Quality Settings:
- Use `veo-3.1-generate-preview` for main narrative clips (1, 2, 4, 5, 6, 7)
- Use `veo-3.1-fast-preview` for montage clips (3A-3F) if needed faster
- Always use 1080p resolution for final quality
- 24fps for cinematic feel
- 16:9 aspect ratio

### Text Overlays (Post-Production):
These are added in editing, not generated:
- Clip 1: "1610. Anyone could discover."
- Clip 2: "2025."
- Clips 3A-3F: Brief text on each ("Debugging..." etc.)
- Clips 8-10: Manifesto text (created in After Effects/Premiere)

### Audio Notes:
- Veo generates native audio, but you may want to replace/enhance in post
- Key audio elements in prompts guide generation but may need mixing
- Music should be custom scored for emotional precision

---

## API Implementation

See `scripts/generate_videos.py` for Python implementation using these prompts.

Each clip should be generated with appropriate wait times and error handling.

Download generated videos within 2 days (Veo retention limit).
