'''
Scenario:
A boy and his father are playing with wooden blocks. They are building a pyramid.
The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.

The program reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.

Note: the height is measured by the number of fully completed layers - if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.

Author: Supriya Jadhav

Version: 1.0

Date Created: Jan 16, 2020

Test Data:

Sample input: 6
Expected output: The height of the pyramid: 3

Sample input: 20
Expected output: The height of the pyramid: 5

Sample input: 1000
Expected output: The height of the pyramid: 44
'''

blocks = int(input("Enter the number of blocks: "))
height = 0
inlayer = 1
while inlayer <= blocks:
	height += 1
	blocks -= inlayer
	inlayer += 1

print("Height of the pyramid:",height)