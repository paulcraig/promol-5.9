'''
FUNC:Jab_1djq_1_5_99_7
PDB:1djq
EC:1.5.99.7
RESI:tyr,his,asp
LOCI:a-169,172,267;
'''
cmd.select('temp0', 'n. ca')
cmd.select('temp1', 'r. tyr')
cmd.select('jessatom0', 'temp0&temp1')
cmd.select('temp2', 'n. cb')
cmd.select('temp3', 'r. tyr')
cmd.select('temp4', 'all w. %s of jessatom0'%(d*1.535200))
cmd.select('temp5', 'br. jessatom0')
cmd.select('jessatom1', 'temp2&temp3&temp4&temp5')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom1'%(d*1.535200))
cmd.select('temp6', 'r. his')
cmd.select('temp7', 'all w. %s of jessatom0'%(d*8.797100))
cmd.select('temp8', 'all w. %s of jessatom1'%(d*8.574900))
cmd.select('jessatom2', 'temp0&temp6&temp7&temp8')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom2'%(d*8.797100))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom2'%(d*8.574900))
cmd.select('temp9', 'all w. %s of jessatom0'%(d*8.645600))
cmd.select('temp10', 'all w. %s of jessatom1'%(d*8.170900))
cmd.select('temp11', 'all w. %s of jessatom2'%(d*1.545300))
cmd.select('temp12', 'br. jessatom2')
cmd.select('jessatom3', 'temp2&temp6&temp9&temp10&temp11&temp12')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom3'%(d*8.645600))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom3'%(d*8.170900))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom3'%(d*1.545300))
cmd.select('temp13', 'r. asp')
cmd.select('temp14', 'r. glu')
cmd.select('temp15', 'all w. %s of jessatom0'%(d*14.907600))
cmd.select('temp16', 'all w. %s of jessatom1'%(d*14.776300))
cmd.select('temp17', 'all w. %s of jessatom2'%(d*8.797100))
cmd.select('temp18', 'all w. %s of jessatom3'%(d*8.736500))
cmd.select('jessatom4', '((temp0&temp13)|(temp0&temp14))&temp15&temp16&temp17&temp18')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom4'%(d*14.907600))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom4'%(d*14.776300))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom4'%(d*8.797100))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom4'%(d*8.736500))
cmd.select('temp19', 'all w. %s of jessatom0'%(d*13.473400))
cmd.select('temp20', 'all w. %s of jessatom1'%(d*13.291600))
cmd.select('temp21', 'all w. %s of jessatom2'%(d*7.383100))
cmd.select('temp22', 'all w. %s of jessatom3'%(d*7.241700))
cmd.select('temp23', 'all w. %s of jessatom4'%(d*1.555400))
cmd.select('temp24', 'br. jessatom4')
cmd.select('jessatom5', '((temp2&temp13)|(temp2&temp14))&temp19&temp20&temp21&temp22&temp23&temp24')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom5'%(d*13.473400))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom5'%(d*13.291600))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom5'%(d*7.383100))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom5'%(d*7.241700))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom5'%(d*1.555400))
cmd.select('Jab_1djq_1_5_99_7', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('temp0')
cmd.delete('temp1')
cmd.delete('temp2')
cmd.delete('temp3')
cmd.delete('temp4')
cmd.delete('temp5')
cmd.delete('temp6')
cmd.delete('temp7')
cmd.delete('temp8')
cmd.delete('temp9')
cmd.delete('temp10')
cmd.delete('temp11')
cmd.delete('temp12')
cmd.delete('temp13')
cmd.delete('temp14')
cmd.delete('temp15')
cmd.delete('temp16')
cmd.delete('temp17')
cmd.delete('temp18')
cmd.delete('temp19')
cmd.delete('temp20')
cmd.delete('temp21')
cmd.delete('temp22')
cmd.delete('temp23')
cmd.delete('temp24')
