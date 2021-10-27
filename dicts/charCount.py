import pprint
message = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce mattis at ante sit amet sollicitudin. In facilisis, felis ut semper elementum, metus ligula porttitor massa, non fermentum metus lorem sit amet sem. Cras rutrum porta metus, vel luctus ipsum ornare nec. Integer quam metus, luctus sit amet interdum vel, fermentum non tortor. Maecenas maximus turpis a nibh dignissim scelerisque. Sed euismod vitae turpis vitae sodales. Nunc at ornare libero, in lobortis metus. Quisque volutpat magna consequat, laoreet magna a, tempus risus. Duis vestibulum sodales massa. Ut leo purus, lobortis at libero at, venenatis finibus elit. Fusce accumsan est quis commodo tristique.
Vestibulum rutrum porttitor dignissim. Quisque id dictum sapien. Sed sodales ligula eu sapien lacinia, a imperdiet enim maximus. Sed diam libero, posuere et ultricies sed, bibendum in lacus. Pellentesque pulvinar placerat congue. Vestibulum mollis laoreet dictum. Duis vitae sapien egestas mauris mollis semper quis a massa. Etiam bibendum lectus quis libero ullamcorper scelerisque.
Aliquam lectus orci, tempus non massa mollis, porttitor consectetur magna. Duis semper neque orci, at lacinia lectus finibus quis. Mauris feugiat sollicitudin eros vitae ultrices. Nullam egestas semper dictum. Suspendisse viverra tellus sapien, id cursus orci imperdiet ac. Duis accumsan lacus sed dui varius laoreet. Nam posuere lacus odio, in dapibus erat suscipit consequat. Curabitur vitae arcu ut ex luctus tempus in sed metus. Curabitur malesuada, neque eu vehicula pharetra, enim nulla faucibus justo, id blandit est turpis nec eros. Morbi nibh dui, imperdiet vel eros in, blandit dapibus lacus. Etiam gravida euismod mattis. Nulla et diam justo.
Praesent rhoncus imperdiet augue, ac placerat magna ornare at. Vivamus eget lobortis diam, eget ullamcorper lacus. Suspendisse ut purus consectetur, laoreet dolor a, tempor tellus. Vestibulum condimentum massa facilisis vehicula porttitor. Praesent at arcu odio. Fusce eleifend, nunc sed pulvinar volutpat, mauris tortor lobortis purus, non pharetra arcu libero blandit est. Vestibulum egestas felis id ex blandit, non condimentum purus fringilla.
Etiam semper laoreet pretium. Praesent at condimentum ante. Nullam mattis nulla vel orci lobortis cursus. Vestibulum placerat lacinia convallis. Nam lobortis felis dolor, sed tempor mauris elementum ac. Praesent luctus sollicitudin dapibus. Etiam laoreet lectus ac imperdiet tempor. Proin tortor nibh, blandit ac posuere quis, sodales vitae justo. Etiam dictum tellus lacus, vitae euismod libero pharetra pretium. Etiam nec semper velit. Curabitur rhoncus, lorem pharetra semper vestibulum, turpis ante blandit libero, a lobortis elit enim vitae diam. In ut lectus enim. Mauris vitae massa enim. Etiam commodo turpis pulvinar pulvinar maximus. Maecenas vehicula tristique scelerisque. 
'''
message2 = 'the quick brown fox jumped over the lazy dog'

count = {}

for character in message2.upper():
  count.setdefault(character, 0)
  count[character] = count[character] + 1

pprint.pprint(count)