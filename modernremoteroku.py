from roku import Roku
rokuls = Roku.discover(timeout=10);
print(rokuls);
ip =  input('IP: ');
roku = Roku(ip);

while True:
	remoteinput = input('Remote Input (i.e. down, up, left, right, back, home, ok, open, text): ');

	if remoteinput == 'down':
		roku.down();
	elif remoteinput == 'up':
		roku.up();
	elif remoteinput == 'left':
		roku.left();
	elif remoteinput == 'right':
		roku.right();
	elif remoteinput == 'back':
		roku.back();
	elif remoteinput == 'home':
		roku.home();
	elif remoteinput == 'ok':
		roku.select();
 	elif remoteinput == 'open':
		appinput = input('APP (i.e. YouTube): ')
		apptolaunch = roku[appinput];
		apptolaunch.launch();
  	elif remoteinput == 'text':
		text = input('TEXT: ');
		roku.literal(text);
	else:
		print('Not a valid command.');

