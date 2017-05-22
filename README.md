test for some font **some words** *italic*
*You **can** combine them*
hyperlink: [my github](https://github.com/yzwxx)
inline code: 
`def print_all(string):print string`
image :
![cifar](https://github.com/zsdonghao/tl-book/blob/master/images/cifar-10.jpg?raw=true)
list:
- first
- second
  - sub first
  - sub second
- third

blockquote:
> okay,here is a block quote

~~strike through~~

==highlight==
horizon line:
-------

![dcgam](https://www.dropbox.com/s/73ualze5ebl209b/train_19_0003.png?raw=true)
This is text with a footnote link at the end. [^1]
[^1]: This is my first footnote

let's have some python code blocks:
```python
def get_data_files2(image_dir):
	# another implementation using glob
	path = image_dir+"**/*.jpg"
	# print(path)
	all_files = glob(path)

	# clean the data 
	for file in all_files:
		img = imread(file, is_grayscale = False)
		# clean data
		if len(img.shape) != 3:
			print(file)
			all_files.remove(file)
	print(len(all_files))
	return all_files
```
quotation:As Kanye West said:

> We're living the future so
> the present is our past

here is a task list:
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item

And a table：

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

==math formula in markdown==

\alpha

$$ \sum_{\forall i}{x_i^{2}} $$

\$\$ x^{2} + y^{2} = z^{2} \$\$

```tex
$$ \sum_{\forall i}{x_i^{2}} $$
```
