Web VPython 3.2

import random

boat = [] 

boat.append(box(pos=vec(0,0,0), color=vec(1,0.8,0.5), size=vec(1.5,0.1,1)))
boat.append(box(pos=vec(0,0.8,0), color=vec(1,0.8,0.5), size=vec(0.05,1.5,0.05)))

boat.append(box(pos=vec(0.66,1.13,0), size=vec(1.3,0.8,0.01), texture="https://png.pngtree.com/png-vector/20251204/ourlarge/pngtree-adorable-guinea-pig-portrait-png-image_18117885.webp"))

wave = []
for i in range(-15,15):
    ry = random.uniform(1,2)
    wave.append(box(pos = vec(i*0.2,-0.3,-0.2), color = color.blue, opacity = 0.5))
    
  
while True :
    rate(80)
    for w in wave : 
        w.size.y = w.size.y + random.uniform(-0.02,0.02)
    k = keysdown()


    if 'a' in k:
        for b in boat:
            b.pos.x -= 0.1


    if 'd' in k:
        for b in boat:
            b.pos.x += 0.1
