from zeep import Client


# Nome dos países disponíveis: https://www.nationsonline.org/oneworld/country_code_list.htm
countryName = input("Digite o nome do país em inglês: ")

client = Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?wsdl')

try:
    isoCode = client.service.CountryISOCode(countryName)
    if "No country found" in isoCode:
        print(f'Nenhum país encontrado com o nome digitado. O nome deve ser em inglês e com letra maiúscula')
        exit()

    capital = client.service.CapitalCity(isoCode)
    currency = client.service.CountryCurrency(isoCode)
    phoneCode = client.service.CountryIntPhoneCode(isoCode)

    print(f'\n\nAs informações do país {countryName} são:\n'
                f'ISO CODE: {isoCode}\n'
                f'Capital: {capital}\n'
                f'Moeda: {currency}\n'
                f'DDI: {phoneCode}\n')

except Exception as e:
    print("Houve um erro ao buscar as informações do país digitado")

