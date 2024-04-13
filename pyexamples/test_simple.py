
import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_Conv("conv1", 64, 3, offset="(0,0,0)", to="(1,0,0)", height=64, depth=64, width=3 ),
    to_Conv("conv2", 64, 64, offset="(1,0,0)", to="(1,0,0)", height=64, depth=64, width=3 ),
    to_Conv("conv3", 64, 64, offset="(1,0,0)", to="(2,0,0)", height=64, depth=64, width=3 ),
    to_Conv("conv4", 64, 64, offset="(2,0,0)", to="(3,0,0)", height=64, depth=64, width=3 ),
    to_Conv("conv5", 32, 64, offset="(3,0,0)", to="(4,0,0)", height=32, depth=32, width=3 ),
    to_Pool("pool1", offset="(0,0,0)", to="(conv5-east)", height=32, depth=32, width=2),
    to_ConvConvRelu("relu1", 1 ,"(0,0,0)", "(pool1-east)", caption="Relu", height=(5,0), width =(0,5)),
    #to_connection( "pool1", "conv2"),
    #to_Conv("conv6", 32, 32, offset="(3,0,0)", to="(4,0,0)", height=32, depth=32, width=2 ),
    #to_Conv("conv7", 32, 32, offset="(4,0,0)", to="(5,0,0)", height=32, depth=32, width=2 ),
    #to_Conv("conv8", 32, 32, offset="(5,0,0)", to="(6,0,0)", height=32, depth=32, width=2 ),
    #to_Conv("conv9", 16, 32, offset="(5,0,0)", to="(6,0,0)", height=16, depth=16, width=2 ),
    #to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=28, depth=28, width=1),
    #to_SoftMax("soft1", 10 ,"(3,0,0)", "(pool1-east)", caption="SOFT"  ),
    #to_connection("pool2", "soft1"),    
    #to_Sum("sum1", offset="(1.5,0,0)", to="(soft1-east)", radius=2.5, opacity=0.6),
    #to_connection("soft1", "sum1"),
    #to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)"),
    
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
