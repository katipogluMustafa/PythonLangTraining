import unittest
import re


def get_list_of_addresses():
  addresses = list()
  with open("addresses.txt", "r", encoding="utf-8") as address_data_file:
    for line in address_data_file:
      addresses.append(line)
  return addresses


class MyTestCase(unittest.TestCase):
  def test_valid_file_read(self):
    input_addresses = get_list_of_addresses()
    self.assertTrue(len(input_addresses) > 0)
    self.assertTrue(len(input_addresses[0]) > 0)

  def test_match_mahalle(self):
    input_addresses = get_list_of_addresses()
    mahalle_regex = ".+MA?H(ALLESİ)?\.?"
    self.assertRegex(input_addresses[5], mahalle_regex)
    self.assertRegex(input_addresses[10], mahalle_regex)
    self.assertRegex(input_addresses[6814], mahalle_regex)

    index = 5
    print(input_addresses[index])
    x = re.search(".+M*A+H(ALLESİ)*\.?\s*", input_addresses[index])
    print(x)

    # for i in range(len(input_addresses)):
    #   self.assertRegex(input_addresses[i], mahalle_regex)

  def test_match_cadde(self):
    input_addresses = get_list_of_addresses()
    cadde_regex = "((\W|^)[A-ZİÖÜÇŞĞ]*\s+)+(CA?D(DE)?(Sİ|SI)?)\.*"
    self.assertRegex(input_addresses[1], cadde_regex)
    self.assertRegex(input_addresses[4], cadde_regex)

    index = 1
    print(input_addresses[index])
    x = re.search("((\W|^)[A-ZİÖÜÇŞĞ]*\s+)+((CA?D(DE)?(Sİ|SI)?)\.*\s*)", input_addresses[index])
    print(x)


  def test_match_sokak(self):
    input_addresses = get_list_of_addresses()
    sokak_regex = "(,\s.*)?([0-9]*\.?)?[A-ZİÖÜÇŞĞ\.]*\s*SO?KA?[KGĞ]?I?"
    self.assertRegex(input_addresses[240], sokak_regex)
    self.assertRegex(input_addresses[354], sokak_regex)
    self.assertRegex(input_addresses[364], sokak_regex)
    self.assertRegex(input_addresses[375], sokak_regex)
    self.assertRegex(input_addresses[385], sokak_regex)
    self.assertRegex(input_addresses[850], sokak_regex)
    self.assertRegex(input_addresses[1001], sokak_regex)

    index = 240
    print(input_addresses[index])
    x = re.search("(,\s.*)?([0-9]*\.?)?([A-ZİÖÜÇŞĞ\.]*)+\s*SO?KA?[KGĞ]?I?\s*", input_addresses[index])
    print(x)


  def test_match_numara(self):
    input_addresses = get_list_of_addresses()
    numara_regex = "\s*NO(:)?\s*([0-9]+(/|-)?\s*([0-9A-Za-z])+)?\s*\W"
    self.assertRegex(input_addresses[1857], numara_regex)
    self.assertRegex(input_addresses[1858], numara_regex)
    self.assertRegex(input_addresses[1859], numara_regex)
    self.assertRegex(input_addresses[1861], numara_regex)
    self.assertRegex(input_addresses[1862], numara_regex)
    self.assertRegex(input_addresses[1863], numara_regex)
    self.assertRegex(input_addresses[1864], numara_regex)
    self.assertRegex(input_addresses[1865], numara_regex)
    self.assertRegex(input_addresses[1866], numara_regex)
    self.assertRegex(input_addresses[1867], numara_regex)

    # self.assertRegex(input_addresses[1860], numara_regex)         IRREGULAR

  def test_bulvar(self):
    input_addresses = get_list_of_addresses()
    bulvar_regex = "(?!.*\.\s.*).*BULVARI"
    self.assertRegex(input_addresses[22], bulvar_regex)
    self.assertRegex(input_addresses[32], bulvar_regex)
    self.assertRegex(input_addresses[37], bulvar_regex)
    self.assertRegex(input_addresses[96], bulvar_regex)
    self.assertRegex(input_addresses[129], bulvar_regex)
    self.assertRegex(input_addresses[126], bulvar_regex)

  def test_asfalt(self):
    input_addresses = get_list_of_addresses()
    asfalt_regex = "(?<=((H|D)\.)).*ASFALTI"
    self.assertRegex(input_addresses[272], asfalt_regex)
    self.assertRegex(input_addresses[478], asfalt_regex)
    self.assertRegex(input_addresses[516], asfalt_regex)
    self.assertRegex(input_addresses[478], asfalt_regex)
    self.assertRegex(input_addresses[536], asfalt_regex)
    #self.assertRegex(input_addresses[1034], asfalt_regex)
    self.assertRegex(input_addresses[1148], asfalt_regex)
    self.assertRegex(input_addresses[6816], asfalt_regex)
    self.assertRegex(input_addresses[5438], asfalt_regex)
    index = 5438
    print(input_addresses[index])
    x = re.search("().*ASFALTI", input_addresses[index])
    print(x)

  def test_match_ofis_no(self):
    input_addresses = get_list_of_addresses()
    numara_regex = "\s*NO::\s*([0-9]+(/|-)?\s*([0-9A-Za-z])+)?\s*\W"
    self.assertRegex(input_addresses[289], numara_regex)
    self.assertRegex(input_addresses[778], numara_regex)

  def test_il_ilce(self):
    input_addresses = get_list_of_addresses()
    asfalt_regex = "\s[A-ZİÖÜÇŞĞ]*\s*/\s*[A-ZİÖÜÇŞĞ]*"
    self.assertRegex(input_addresses[5438], asfalt_regex)
    self.assertRegex(input_addresses[1650], asfalt_regex)

    index = 5040
    print(input_addresses[index])
    x = re.search("\s[A-ZİÖÜÇŞĞ]*\s*/\s*[A-ZİÖÜÇŞĞ]*", input_addresses[index])
    print(x)

  def test_apt(self):
    input_addresses = get_list_of_addresses()
    apt_regex = "\s*[A-ZİÖÜÇŞĞ]*\sAPT\."
    self.assertRegex(input_addresses[1730], apt_regex)


if __name__ == '__main__':
  unittest.main()
