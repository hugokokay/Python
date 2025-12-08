altura=float(input('Digite a altura da parede '))
largura=float(input('Digite a largura da parede '))
area=altura*largura
print('Sua parede tem {}x{} e sua área é de {}m²' .format(altura, largura, area))
print('Para pintar a parede você precisa de {} litros de tinta' .format(area/2))

