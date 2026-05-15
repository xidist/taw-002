# risograph - supermarketsallad

Created: May 10, 2026 8:52 AM
Tags: ai, creativecode, risograph, stream, supermarketsallad, touchdesigner
twitch: https://www.twitch.tv/tinyspigot

![Image 5-10-26 at 8.41 AM.jpg](risograph%20-%20supermarketsallad/Image_5-10-26_at_8.41_AM.jpg)

![image.png](risograph%20-%20supermarketsallad/image.png)

![image.png](risograph%20-%20supermarketsallad/image%201.png)

![image.png](risograph%20-%20supermarketsallad/image%202.png)

![image.png](risograph%20-%20supermarketsallad/image%203.png)

# ramp colors

is there an easier way to use my existing ramp?Yes, there is an easier way to use your existing ramp without manual layering.**The "Lookup" Shortcut**The most efficient way to use an existing Ramp TOP is with a [**Lookup TOP**](https://derivative.ca/UserGuide/Lookup_TOP). This operator uses the brightness of your `TOTONE` output to "look up" the colors in your ramp. [[1](https://www.youtube.com/shorts/C_LQyOQ4lLc), [2](https://www.reddit.com/r/TouchDesigner/comments/1jcvl25/changing_the_horizon_of_a_ramp/)]
1. **Connect `TOTONE` to Input 1** of the Lookup TOP.
2. **Connect your existing Ramp to Input 2**.
3. The Lookup TOP will automatically map the colors from left-to-right based on the input's luminosity. [[1](https://www.reddit.com/r/TouchDesigner/comments/1jcvl25/changing_the_horizon_of_a_ramp/)]**Customizing the Ramp Effortlessly**If the ramp itself is the problem, you can speed up the process with these tricks:
• **The "Phase" Trick:** Use the **Phase** parameter on your Ramp TOP to "cycle" the colors through your image. [[1](https://www.youtube.com/watch?v=oeX1ipQGoek), [2](https://www.reddit.com/r/TouchDesigner/comments/1enjf6b/has_anyone_figured_out_how_to_create/)]
• **External .TOX Tools:** For even more control, look into community-made tools like [**MetaRamp**](https://derivative.ca/community-post/asset/metaramp-top/65699), which makes animating and referencing ramp keys much simpler than the default interface. [[1](https://derivative.ca/community-post/asset/metaramp-top/65699)]
• **Direct DAT Editing:** You can also point the **DAT** parameter on the Ramp TOP to a table. Any changes you make to that table will update the ramp instantly. [[1](https://derivative.ca/UserGuide/Ramp_TOP)][**Four point gradient? - Beginners - TouchDesigner forum**TouchDesigner forum](https://forum.derivative.ca/t/four-point-gradient/287217)[**Diamond, triangle and other shaped ramps - Beginners - TouchDesigner forum**TouchDesigner forum](https://forum.derivative.ca/t/diamond-triangle-and-other-shaped-ramps/646965)[**Ramp TOP into Circle SOP? - Beginners - TouchDesigner forum**TouchDesigner forum](https://forum.derivative.ca/t/ramp-top-into-circle-sop/202262)[**ramp tunnel in TouchDesigner - YouTube**YouTube](https://www.youtube.com/watch?v=Ci-QqYXje0o)[**Ramps in TouchDesigner - YouTube**YouTube](https://www.youtube.com/watch?v=vdje-kWmhjk)[**Solved: Stylized Ramps in MaterialX (Maya / Arnold) possible in LookdevX? - Autodesk Community**Forums, Autodesk](https://forums.autodesk.com/t5/arnold-for-maya-forum/stylized-ramps-in-materialx-maya-arnold-possible-in-lookdevx/td-p/13890241)[**Mapping – Remapping UV- and Pixel Maps for Multiscreen – The NODE Institute**The NODE Institute](https://thenodeinstitute.org/courses/ss25-td-mapping-remapping-uv-and-pixel-maps/)[**Triggering One-Shot Ramps: trigger CHOP, timer CHOP and Cook time - General TouchDesigner Discussion - TouchDesigner forum**TouchDesigner forum](https://forum.derivative.ca/t/triggering-one-shot-ramps-trigger-chop-timer-chop-and-cook-time/222754)[**Building a Live Custom Audio-Reactive Visualization in Touchdesigner | by Colin Patrick Reid | Medium**Medium](https://medium.com/@colinpatrickreid/building-a-live-custom-audio-reactive-visualization-in-touchdesigner-c195b7f591a7)[**RealRamp - FREE TouchDesigner Component - What's wrong with Ramp TOP?! - YouTube**YouTube](https://www.youtube.com/watch?v=6y2NN1RAqdQ)[**lookup TOP / Ramp - Beginners - TouchDesigner forum**TouchDesigner forum](https://forum.derivative.ca/t/lookup-top-ramp/12007)[**How do I loop a remap colour gradient? Is it a case of continuously copying + pasting knots (that seems like overkill) If I try and tile the material, the ramp doesn't**Facebook](https://www.facebook.com/groups/RedshiftRender/posts/1662716100844260/)[**Process Blog | Jordan McInnes Portfolio Site | 3D Generalist from Sydney who loves to Rig and Script | Page 3**Jordan McInnes Portfolio Site - WordPress.com](https://jordanmcinnes.wordpress.com/blog/page/3/)[**MetaRamp TOP | Derivative**TouchDesigner](https://derivative.ca/community-post/asset/metaramp-top/65699)[**Tutorials | Page 22 | Derivative**TouchDesigner](https://derivative.ca/tutorials/1000?page=21)[**Updated Toon Shader for Blender 4.4+ (Maybe works for older versions with some tweaks?? IDK) - YouTube**YouTube](https://www.youtube.com/watch?v=cckTbqLhHGg)[**How to scale a ramp circle mask on a grid image in Redshift Render?**Facebook](https://www.facebook.com/groups/RedshiftRender/posts/2129598660822666/)[**Rendering prehistoric animals |**WordPress.com](https://dotnametechblog.wordpress.com/another-tut-03/)[**texturing - How to get a Color Ramp gradient to rotate from the centre of a cube? - Blender Stack Exchange**Blender Stack Exchange](https://blender.stackexchange.com/questions/346075/how-to-get-a-color-ramp-gradient-to-rotate-from-the-centre-of-a-cube)[**Playing with Object Tracking in TouchDesigner using the MediaPipe plugin I co-created with @domscott.art. Try it with 🎧. Really excited I got the audio panning**Instagram](https://www.instagram.com/reel/DKz6E8SR1jb/)**Are you trying to apply one ramp to the whole image, or do you want different colors for each ink layer?**

## ramp colors debug

![image.png](risograph%20-%20supermarketsallad/image%204.png)

### d**ebug: output twotone riso ← black screen fix!**

**the trick is to click this blue dot!**

![image.png](risograph%20-%20supermarketsallad/image%205.png)