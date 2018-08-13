from roku import Roku
rokuls = Roku.discover(timeout=10);
print(rokuls);
ip =  input('IP: ');
roku = Roku(ip);
appinput = input('APP (i.e. YouTube): ')
apptolaunch = roku[appinput];
apptolaunch.launch();
