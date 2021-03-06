'''
FUNC:A_1wnw_1_14_99_3
PDB:1wnw
EC:1.14.99.3
RESI:asn,gly
LOCI:a-136,140;
'''
cmd.select('asn1', 'n. CB&r. asn w. %s of n. O&r. gly'%(d*9.01))
cmd.select('asn2', 'n. CB&r. asn w. %s of n. C&r. gly'%(d*8.30))
cmd.select('asn3', 'n. CB&r. asn w. %s of n. CA&r. gly'%(d*7.03))
cmd.select('asn4', 'n. CB&r. asn w. %s of n. N&r. gly'%(d*7.16))
cmd.select('asn5', 'n. CG&r. asn w. %s of n. O&r. gly'%(d*8.16))
cmd.select('asn6', 'n. CG&r. asn w. %s of n. C&r. gly'%(d*7.61))
cmd.select('asn7', 'n. CG&r. asn w. %s of n. CA&r. gly'%(d*6.58))
cmd.select('asn8', 'n. CG&r. asn w. %s of n. N&r. gly'%(d*7.08))
cmd.select('asn9', 'n. OD1&r. asn w. %s of n. O&r. gly'%(d*7.00))
cmd.select('asn10', 'n. OD1&r. asn w. %s of n. C&r. gly'%(d*6.44))
cmd.select('asn11', 'n. OD1&r. asn w. %s of n. CA&r. gly'%(d*5.54))
cmd.select('asn12', 'n. OD1&r. asn w. %s of n. N&r. gly'%(d*6.19))
cmd.select('asn13', 'n. ND2&r. asn w. %s of n. O&r. gly'%(d*8.98))
cmd.select('asn14', 'n. ND2&r. asn w. %s of n. C&r. gly'%(d*8.60))
cmd.select('asn15', 'n. ND2&r. asn w. %s of n. CA&r. gly'%(d*7.70))
cmd.select('asn16', 'n. ND2&r. asn w. %s of n. N&r. gly'%(d*8.34))
cmd.select('asn17', 'n. O&r. asn w. %s of n. O&r. gly'%(d*7.48))
cmd.select('asn18', 'n. O&r. asn w. %s of n. C&r. gly'%(d*6.39))
cmd.select('asn19', 'n. O&r. asn w. %s of n. CA&r. gly'%(d*5.42))
cmd.select('asn20', 'n. O&r. asn w. %s of n. N&r. gly'%(d*5.01))
cmd.select('asn21', 'n. C&r. asn w. %s of n. O&r. gly'%(d*8.43))
cmd.select('asn22', 'n. C&r. asn w. %s of n. C&r. gly'%(d*7.39))
cmd.select('asn23', 'n. C&r. asn w. %s of n. CA&r. gly'%(d*6.21))
cmd.select('asn24', 'n. C&r. asn w. %s of n. N&r. gly'%(d*5.75))
cmd.select('asn25', 'n. CA&r. asn w. %s of n. O&r. gly'%(d*8.47))
cmd.select('asn26', 'n. CA&r. asn w. %s of n. C&r. gly'%(d*7.59))
cmd.select('asn27', 'n. CA&r. asn w. %s of n. CA&r. gly'%(d*6.21))
cmd.select('asn28', 'n. CA&r. asn w. %s of n. N&r. gly'%(d*5.98))
cmd.select('asn29', 'n. N&r. asn w. %s of n. O&r. gly'%(d*9.58))
cmd.select('asn30', 'n. N&r. asn w. %s of n. C&r. gly'%(d*8.69))
cmd.select('asn31', 'n. N&r. asn w. %s of n. CA&r. gly'%(d*7.23))
cmd.select('asn32', 'n. N&r. asn w. %s of n. N&r. gly'%(d*6.77))
cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18&br. asn19&br. asn20&br. asn21&br. asn22&br. asn23&br. asn24&br. asn25&br. asn26&br. asn27&br. asn28&br. asn29&br. asn30&br. asn31&br. asn32')
cmd.delete('asn1')
cmd.delete('asn2')
cmd.delete('asn3')
cmd.delete('asn4')
cmd.delete('asn5')
cmd.delete('asn6')
cmd.delete('asn7')
cmd.delete('asn8')
cmd.delete('asn9')
cmd.delete('asn10')
cmd.delete('asn11')
cmd.delete('asn12')
cmd.delete('asn13')
cmd.delete('asn14')
cmd.delete('asn15')
cmd.delete('asn16')
cmd.delete('asn17')
cmd.delete('asn18')
cmd.delete('asn19')
cmd.delete('asn20')
cmd.delete('asn21')
cmd.delete('asn22')
cmd.delete('asn23')
cmd.delete('asn24')
cmd.delete('asn25')
cmd.delete('asn26')
cmd.delete('asn27')
cmd.delete('asn28')
cmd.delete('asn29')
cmd.delete('asn30')
cmd.delete('asn31')
cmd.delete('asn32')
cmd.select('gly1', 'n. O&r. gly w. %s of n. CB&asn'%(d*9.01))
cmd.select('gly2', 'n. O&r. gly w. %s of n. CG&asn'%(d*8.16))
cmd.select('gly3', 'n. O&r. gly w. %s of n. OD1&asn'%(d*7.00))
cmd.select('gly4', 'n. O&r. gly w. %s of n. ND2&asn'%(d*8.98))
cmd.select('gly5', 'n. O&r. gly w. %s of n. O&asn'%(d*7.48))
cmd.select('gly6', 'n. O&r. gly w. %s of n. C&asn'%(d*8.43))
cmd.select('gly7', 'n. O&r. gly w. %s of n. CA&asn'%(d*8.47))
cmd.select('gly8', 'n. O&r. gly w. %s of n. N&asn'%(d*9.58))
cmd.select('gly9', 'n. C&r. gly w. %s of n. CB&asn'%(d*8.30))
cmd.select('gly10', 'n. C&r. gly w. %s of n. CG&asn'%(d*7.61))
cmd.select('gly11', 'n. C&r. gly w. %s of n. OD1&asn'%(d*6.44))
cmd.select('gly12', 'n. C&r. gly w. %s of n. ND2&asn'%(d*8.60))
cmd.select('gly13', 'n. C&r. gly w. %s of n. O&asn'%(d*6.39))
cmd.select('gly14', 'n. C&r. gly w. %s of n. C&asn'%(d*7.39))
cmd.select('gly15', 'n. C&r. gly w. %s of n. CA&asn'%(d*7.59))
cmd.select('gly16', 'n. C&r. gly w. %s of n. N&asn'%(d*8.69))
cmd.select('gly17', 'n. CA&r. gly w. %s of n. CB&asn'%(d*7.03))
cmd.select('gly18', 'n. CA&r. gly w. %s of n. CG&asn'%(d*6.58))
cmd.select('gly19', 'n. CA&r. gly w. %s of n. OD1&asn'%(d*5.54))
cmd.select('gly20', 'n. CA&r. gly w. %s of n. ND2&asn'%(d*7.70))
cmd.select('gly21', 'n. CA&r. gly w. %s of n. O&asn'%(d*5.42))
cmd.select('gly22', 'n. CA&r. gly w. %s of n. C&asn'%(d*6.21))
cmd.select('gly23', 'n. CA&r. gly w. %s of n. CA&asn'%(d*6.21))
cmd.select('gly24', 'n. CA&r. gly w. %s of n. N&asn'%(d*7.23))
cmd.select('gly25', 'n. N&r. gly w. %s of n. CB&asn'%(d*7.16))
cmd.select('gly26', 'n. N&r. gly w. %s of n. CG&asn'%(d*7.08))
cmd.select('gly27', 'n. N&r. gly w. %s of n. OD1&asn'%(d*6.19))
cmd.select('gly28', 'n. N&r. gly w. %s of n. ND2&asn'%(d*8.34))
cmd.select('gly29', 'n. N&r. gly w. %s of n. O&asn'%(d*5.01))
cmd.select('gly30', 'n. N&r. gly w. %s of n. C&asn'%(d*5.75))
cmd.select('gly31', 'n. N&r. gly w. %s of n. CA&asn'%(d*5.98))
cmd.select('gly32', 'n. N&r. gly w. %s of n. N&asn'%(d*6.77))
cmd.select('gly',' br. gly1&br. gly2&br. gly3&br. gly4&br. gly5&br. gly6&br. gly7&br. gly8&br. gly9&br. gly10&br. gly11&br. gly12&br. gly13&br. gly14&br. gly15&br. gly16&br. gly17&br. gly18&br. gly19&br. gly20&br. gly21&br. gly22&br. gly23&br. gly24&br. gly25&br. gly26&br. gly27&br. gly28&br. gly29&br. gly30&br. gly31&br. gly32')
cmd.delete('gly1')
cmd.delete('gly2')
cmd.delete('gly3')
cmd.delete('gly4')
cmd.delete('gly5')
cmd.delete('gly6')
cmd.delete('gly7')
cmd.delete('gly8')
cmd.delete('gly9')
cmd.delete('gly10')
cmd.delete('gly11')
cmd.delete('gly12')
cmd.delete('gly13')
cmd.delete('gly14')
cmd.delete('gly15')
cmd.delete('gly16')
cmd.delete('gly17')
cmd.delete('gly18')
cmd.delete('gly19')
cmd.delete('gly20')
cmd.delete('gly21')
cmd.delete('gly22')
cmd.delete('gly23')
cmd.delete('gly24')
cmd.delete('gly25')
cmd.delete('gly26')
cmd.delete('gly27')
cmd.delete('gly28')
cmd.delete('gly29')
cmd.delete('gly30')
cmd.delete('gly31')
cmd.delete('gly32')
cmd.select('A_1wnw_1_14_99_3', 'asn|gly')
cmd.delete('asn')
cmd.delete('gly')
