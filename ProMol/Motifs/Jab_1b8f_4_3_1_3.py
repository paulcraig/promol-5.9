'''
FUNC:Jab_1b8f_4_3_1_3
PDB:1b8f
EC:4.3.1.3
RESI:ala,ser,gly,tyr,glu
LOCI:a-142,143,144,280,414;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. ala'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. ala'
jesstemp4 ='jessatom0 x. %s'%(1.515000+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.515000+(d*0.300000)))
jesstemp6 ='r. ser'
jesstemp7 ='r. thr'
jesstemp8 ='jessatom0 x. %s'%(3.757200+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(4.433900+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(3.757200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(4.433900+(d*0.300000)))
jesstemp10 ='jessatom0 x. %s'%(4.949000+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(5.403500+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(1.343300+(d*0.300000))
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp2+')&('+jesstemp6+'))|(('+jesstemp2+')&('+jesstemp7+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.949000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.403500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.343300+(d*0.300000)))
jesstemp14 ='r. gly'
jesstemp15 ='jessatom0 x. %s'%(3.040100+(d*0.300000))
jesstemp16 ='jessatom1 x. %s'%(4.514700+(d*0.300000))
jesstemp17 ='jessatom2 x. %s'%(3.444100+(d*0.300000))
jesstemp18 ='jessatom3 x. %s'%(4.696500+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(3.040100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(4.514700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(3.444100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(4.696500+(d*0.300000)))
jesstemp19 ='n.  c  '
jesstemp20 ='jessatom0 x. %s'%(3.959200+(d*0.300000))
jesstemp21 ='jessatom1 x. %s'%(5.433800+(d*0.300000))
jesstemp22 ='jessatom2 x. %s'%(4.363200+(d*0.300000))
jesstemp23 ='jessatom3 x. %s'%(5.423700+(d*0.300000))
jesstemp24 ='jessatom4 x. %s'%(1.575600+(d*0.300000))
jesstemp25 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp19+')&('+jesstemp14+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(3.959200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(5.433800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.363200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(5.423700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.575600+(d*0.300000)))
jesstemp26 ='r. tyr'
jesstemp27 ='jessatom0 x. %s'%(42.793700+(d*0.300000))
jesstemp28 ='jessatom1 x. %s'%(42.844200+(d*0.300000))
jesstemp29 ='jessatom2 x. %s'%(46.399400+(d*0.300000))
jesstemp30 ='jessatom3 x. %s'%(47.651800+(d*0.300000))
jesstemp31 ='jessatom4 x. %s'%(43.581500+(d*0.300000))
jesstemp32 ='jessatom5 x. %s'%(43.288600+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(42.793700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(42.844200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(46.399400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(47.651800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(43.581500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(43.288600+(d*0.300000)))
jesstemp33 ='jessatom0 x. %s'%(42.127100+(d*0.300000))
jesstemp34 ='jessatom1 x. %s'%(42.127100+(d*0.300000))
jesstemp35 ='jessatom2 x. %s'%(45.763100+(d*0.300000))
jesstemp36 ='jessatom3 x. %s'%(47.005400+(d*0.300000))
jesstemp37 ='jessatom4 x. %s'%(43.005800+(d*0.300000))
jesstemp38 ='jessatom5 x. %s'%(42.743200+(d*0.300000))
jesstemp39 ='jessatom6 x. %s'%(1.565500+(d*0.300000))
jesstemp40 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp2+')&('+jesstemp26+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(42.127100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(42.127100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(45.763100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(47.005400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(43.005800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(42.743200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.565500+(d*0.300000)))
jesstemp41 ='r. glu'
jesstemp42 ='r. asp'
jesstemp43 ='jessatom0 x. %s'%(7.989100+(d*0.300000))
jesstemp44 ='jessatom1 x. %s'%(6.847800+(d*0.300000))
jesstemp45 ='jessatom2 x. %s'%(7.665900+(d*0.300000))
jesstemp46 ='jessatom3 x. %s'%(7.292200+(d*0.300000))
jesstemp47 ='jessatom4 x. %s'%(10.231300+(d*0.300000))
jesstemp48 ='jessatom5 x. %s'%(11.009000+(d*0.300000))
jesstemp49 ='jessatom6 x. %s'%(47.863900+(d*0.300000))
jesstemp50 ='jessatom7 x. %s'%(47.005400+(d*0.300000))
cmd.select('jessatom8', '(((('+jesstemp0+')&('+jesstemp41+'))|(('+jesstemp0+')&('+jesstemp42+')))&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(7.989100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(6.847800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(7.665900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(7.292200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(10.231300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(11.009000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(47.863900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(47.005400+(d*0.300000)))
jesstemp51 ='jessatom0 x. %s'%(7.160900+(d*0.300000))
jesstemp52 ='jessatom1 x. %s'%(6.201400+(d*0.300000))
jesstemp53 ='jessatom2 x. %s'%(6.605400+(d*0.300000))
jesstemp54 ='jessatom3 x. %s'%(6.181200+(d*0.300000))
jesstemp55 ='jessatom4 x. %s'%(9.201100+(d*0.300000))
jesstemp56 ='jessatom5 x. %s'%(9.847500+(d*0.300000))
jesstemp57 ='jessatom6 x. %s'%(47.672000+(d*0.300000))
jesstemp58 ='jessatom7 x. %s'%(46.853900+(d*0.300000))
jesstemp59 ='jessatom8 x. %s'%(1.535200+(d*0.300000))
jesstemp60 ='br. jessatom8'
cmd.select('jessatom9', '(((('+jesstemp2+')&('+jesstemp41+'))|(('+jesstemp2+')&('+jesstemp42+')))&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(7.160900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(6.201400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(6.605400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(6.181200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(9.201100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(9.847500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(47.672000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(46.853900+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(1.535200+(d*0.300000)))
cmd.select('Jab_1b8f_4_3_1_3', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
cmd.delete('jessatom9')
