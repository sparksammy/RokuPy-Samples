from roku import Roku
rokuls = Roku.discover(timeout=10);
print(rokuls);
ip =  input('IP: ');
roku = Roku(ip);

while True:
	roku.down();
	roku.down();
	roku.down();
	roku.down();
	roku.up();
	roku.up();
	roku.left();
	roku.left();
	roku.right();
	roku.right();
	roku.right();
