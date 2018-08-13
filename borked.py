from roku import Roku
rokuls = Roku.discover(timeout=10);
print(rokuls);
ip =  input('IP: ');
roku = Roku(ip);
rokuapps = roku.apps;
print(r[rokuapps]);
