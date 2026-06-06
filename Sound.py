import sounddevice as sd
import pygame

fs = 44100
chunk = 1024
data = [0.0] * chunk

SIZE = (800,600)
BG_COLOR = (0,0,0)
LINE_COLOR = (0,255,0)
FPS = 60

pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption('Sound Example')

def audio_callback(in_data, frames, time_info, status):
    global data
    if status:
        print(status)
    data = [sample * (SIZE[1]/2) for sample in in_data[:,0].tolist()]

stream = sd.InputStream(callback=audio_callback,channels=1,samplerate=fs,blocksize=chunk,dtype='float32')
stream.start()

#print(sd.query_devices())
running =True
while running:
    screen.fill(BG_COLOR)

    points = []
    for i,sample in enumerate(data):
        x = int((i*SIZE[0]/chunk))
        y = int(SIZE[1]/2 + sample)
        points.append((x,y))

    if len(points)>1:
        pygame.draw.lines(screen,LINE_COLOR,False,points)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(FPS)
stream.close()
quit()