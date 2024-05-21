import cx_Freeze
import os

img_dir = os.path.join(os.path.dirname(__file__),"img")
snd_dir = os.path.join(os.path.dirname(__file__),"snd")

os.environ['TCL_LIBRARY'] = "C:\\python\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\python\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("sky_war.py",icon="icon.ico")]

cx_Freeze.setup(
    name = "Don't Crash",
    options = {"build_exe":{"packages":["pygame"],
                            "include_files":[os.path.join('C:\python','DLLs','tk86t.dll'),
                                             os.path.join('C:\python','DLLs','tcl86t.dll'),
                                             "icon.ico",
                                             "icon.png",
                                             # art
                                             os.path.join(img_dir,"background.jpg"),
                                             os.path.join(img_dir,"boss1.png"),
                                             os.path.join(img_dir,"boss2.png"),
                                             os.path.join(img_dir,"boss3.png"),
                                             os.path.join(img_dir,"bulletup.png"),
                                             os.path.join(img_dir,"dart.png"),
                                             os.path.join(img_dir,"down.png"),
                                             os.path.join(img_dir,"enemy1img.png"),
                                             os.path.join(img_dir,"enemy2img.png"),
                                             os.path.join(img_dir,"enemy3.png"),
                                             os.path.join(img_dir,"gameover.jpg"),
                                             os.path.join(img_dir,"healthup.png"),
                                             os.path.join(img_dir,"infobackground.jpg"),
                                             os.path.join(img_dir,"introbackground.png"),
                                             os.path.join(img_dir,"left.png"),
                                             os.path.join(img_dir,"left.png"),
                                             os.path.join(img_dir,"m1.png"),
                                             os.path.join(img_dir,"m2.png"),
                                             os.path.join(img_dir,"m3.png"),
                                             os.path.join(img_dir,"m4.png"),
                                             os.path.join(img_dir,"m5.png"),
                                             os.path.join(img_dir,"m6.png"),
                                             os.path.join(img_dir,"m7.png"),
                                             os.path.join(img_dir,"missile.png"),
                                             os.path.join(img_dir,"missilesymbol.png"),
                                             os.path.join(img_dir,"missileup.png"),
                                             os.path.join(img_dir,"mylaser.png"),
                                             os.path.join(img_dir,"player.png"),
                                             os.path.join(img_dir,"regularExplosion00.png"),
                                             os.path.join(img_dir,"regularExplosion01.png"),
                                             os.path.join(img_dir,"regularExplosion02.png"),
                                             os.path.join(img_dir,"regularExplosion03.png"),
                                             os.path.join(img_dir,"regularExplosion04.png"),
                                             os.path.join(img_dir,"regularExplosion05.png"),
                                             os.path.join(img_dir,"regularExplosion06.png"),
                                             os.path.join(img_dir,"regularExplosion07.png"),
                                             os.path.join(img_dir,"regularExplosion08.png"),
                                             os.path.join(img_dir,"right.png"),
                                             os.path.join(img_dir,"roundbullet.png"),
                                             os.path.join(img_dir,"shield.png"),
                                             os.path.join(img_dir,"shieldsymbol.png"),
                                             os.path.join(img_dir,"shieldup.png"),
                                             os.path.join(img_dir,"sonicExplosion00.png"),
                                             os.path.join(img_dir,"sonicExplosion01.png"),
                                             os.path.join(img_dir,"sonicExplosion02.png"),
                                             os.path.join(img_dir,"sonicExplosion03.png"),
                                             os.path.join(img_dir,"sonicExplosion04.png"),
                                             os.path.join(img_dir,"sonicExplosion05.png"),
                                             os.path.join(img_dir,"sonicExplosion06.png"),
                                             os.path.join(img_dir,"sonicExplosion07.png"),
                                             os.path.join(img_dir,"sonicExplosion08.png"),
                                             os.path.join(img_dir,"space.png"),
                                             os.path.join(img_dir,"speedup.png"),
                                             os.path.join(img_dir,"up.png"),
                                             os.path.join(img_dir,"x.png"),
                                             os.path.join(img_dir,"musik_hidup.png"),
                                             os.path.join(img_dir,"musik_mati.png"),
                                             os.path.join(img_dir,"start.png"),
                                             os.path.join(img_dir,"back.png"),
                                             os.path.join(img_dir,"exit.png"),
                                             os.path.join(img_dir,"kembali.png"),
                                             os.path.join(img_dir,"replay.png"),
                                             os.path.join(img_dir,"infoimg.png"),
                                             os.path.join(img_dir,"lanjut.png"),
                                             os.path.join(img_dir,"jeda.png"),
                                             os.path.join(img_dir,"gameoverimg.png"),

                                             # sound
                                             os.path.join(snd_dir,"bulletup.wav"),
                                             os.path.join(snd_dir,"explodebg.wav"),
                                             os.path.join(snd_dir,"explodedeath.wav"),
                                             os.path.join(snd_dir,"explodesm.wav"),
                                             os.path.join(snd_dir,"game.mp3"),
                                             os.path.join(snd_dir,"healthup.wav"),
                                             os.path.join(snd_dir,"info.mp3"),
                                             os.path.join(snd_dir,"liveup.wav"),
                                             os.path.join(snd_dir,"loose.mp3"),
                                             os.path.join(snd_dir,"missile.wav"),
                                             os.path.join(snd_dir,"missileup.wav"),
                                             os.path.join(snd_dir,"shield.wav"),
                                             os.path.join(snd_dir,"shieldup.wav"),
                                             os.path.join(snd_dir,"shoot.wav"),
                                             os.path.join(snd_dir,"speedup.wav"),
                                             os.path.join(snd_dir,"theme.mp3")]}},
    version = "1",
    executables = executables
    )
