import argparse, sys, struct

class Flash:
    def ActionScript(input, output):
        with open(input,'rb') as l:
            script=open(output,'w')
            script.write('function initObjectPos()'+'\n')
            script.write('{'+'\n')
            l.read(5)
            objectcount=struct.unpack('>h',l.read(2))[0]
            print('adding '+str(objectcount)+' objects...')
            for object in range(objectcount):
                objectid=struct.pack('>c',l.read(1))[0]
                l.read(1)
                l.read(1)
                width=struct.unpack('>h',l.read(2))[0]#+330
                l.read(1)
                l.read(1)
                height=struct.unpack('>h',l.read(2))[0]
                if objectid==1: #spike
                    script.write('  addS('+str(width)+','+str(height)+');'+'\n')
                elif objectid==0: #block
                    script.write('  addB('+str(width)+','+str(height)+');'+'\n')
                elif objectid==2: #pit
                    script.write('  addP('+str(width)+','+str(height)+');'+'\n')
            l.read(2)
            levelend=struct.unpack('>h',l.read(2))[0]
            l.read(3)
            bkgcount=struct.pack('>c',l.read(1))[0]
            for bkg in range(bkgcount):
                l.read(2)
                bkgwidth=struct.unpack('>h',l.read(2))[0]
                l.read(4)
                bkgcolor=struct.pack('>c',l.read(1))[0]
                if bkgcolor==0: #blue
                    continue
                elif bkgcolor==1: #yellow
                    continue
                elif bkgcolor==2: #green
                    continue
                elif bkgcolor==3: #violet
                    continue
                elif bkgcolor==4: #pink
                    continue
                elif bkgcolor==5: #black
                    continue

            script.write('}')

parser=argparse.ArgumentParser(description='Converts Impossible Game DAT files to Flash (ActionScript)')
parser.add_argument('-i', action='store', dest='i', help='Input file')
parser.add_argument('-o', action='store', dest='o', help='Output file')
args = vars(parser.parse_args())

if args['i'] == None or args['o'] == None:
	parser.print_help(sys.stderr)
	quit()

Flash.ActionScript(args['i'], args['o'])