from roku import Roku
rokuls = Roku.discover(timeout=10);
print(rokuls);
ip =  input('IP: ');
roku = Roku(ip);
text = input('TEXT: ');
roku.literal(text);
