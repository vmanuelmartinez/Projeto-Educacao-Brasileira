from fpdf import FPDF

class PDF(FPDF):

    def titulo(self, label):
        self.set_font('helvetica', 'B', size=20)
        self.cell(0, 60, label, 0, 1, 'C')

    def subtitulo(self, label):
        self.set_font('helvetica', 'I', size=16)
        self.cell(0, 10, label, 0, 1, 'C')

    def paragrafo(self, text):
        self.set_font('helvetica', 'I', size=12)
        self.multi_cell(0, 7, text)
        self.ln()
        

    def imagem(self, img, x, y, w):
        self.image(img, x, y, w)
        

pdf = PDF()
#------CAPA-------#
pdf.add_page()
pdf.imagem("image-capa.png", 10, 5, 180)

# ---- Primeira Página ---- #
pdf.add_page()

pdf.titulo("Desigualdade na Educação Brasileira: Um Estudo")

pdf.paragrafo("A desigualdade na educação brasileira é um problema complexo e persistente que afeta a qualidade e o acesso à educação em diferentes regiões do país. Apesar dos avanços significativos nas últimas décadas, as disparidades entre as áreas urbanas e rurais, bem como entre diferentes classes socioeconômicas, continuam a ser um desafio importante.")

pdf.image("Gráfico-matriculas-Rede-Publica-Ensino-Fundamental.png", 30, 100, 140)


# ---- Segunda Página ---- #
pdf.add_page()
pdf.titulo("Analfabetismo em diversas regiões do Brasil") #Nordeste
pdf.paragrafo("O analfabetismo na região Nordeste do Brasil continua a ser um desafio significativo, refletindo disparidades históricas e socioeconômicas.")

pdf.paragrafo("Apesar dos esforços para melhorar a educação, muitas áreas ainda enfrentam altos índices de analfabetismo devido a fatores como a falta de infraestrutura, baixa qualidade do ensino e dificuldades econômicas.")

pdf.paragrafo("A região enfrenta desafios significativos devido a fatores como a escassez de recursos educacionais, infraestrutura precária e baixos investimentos em educação. Esses fatores afetam principalmente as áreas rurais e as populações em situação de vulnerabilidade")

pdf.paragrafo(" Para reduzir as taxas de analfabetismo e promover o acesso à educação de qualidade, é essencial implementar políticas públicas eficazes e programas de alfabetização adaptados às necessidades locais.")

pdf.image("Analfabetismo-nordeste.png", 20, 170, 170)

# ---- Terceira Página ---- #
pdf.add_page()
pdf.titulo("Região Norte")
pdf.paragrafo("Região Norte \n O analfabetismo na região Norte do Brasil é uma questão preocupante, exacerbada pelas vastas distâncias e pela dificuldade de acesso a serviços educacionais em áreas remotas.")

pdf.paragrafo("Além disso, a presença de populações indígenas e comunidades ribeirinhas, muitas vezes distantes dos centros urbanos, intensifica o problema. Para combater o analfabetismo na região Norte, é crucial desenvolver iniciativas educacionais que atendam às especificidades locais e promovam a inclusão de todos os grupos sociais.")

pdf.image("Analfabetismo-Regiao-Norte.png", 20, 130, 170)

# ---- Quarta Página ---- #
pdf.add_page()
pdf.titulo("Região Oeste")
pdf.paragrafo("O analfabetismo na região Oeste do Brasil é um problema significativo, especialmente nas áreas rurais e menos desenvolvidas. A escassez de escolas e a baixa oferta de cursos de alfabetização contribuem para a persistência desse desafio. Fatores como a falta de recursos, infraestrutura inadequada e a difícil acessibilidade em áreas isoladas agravam a situação.")

pdf.paragrafo("Muitos moradores enfrentam barreiras adicionais, como a necessidade de trabalhar desde cedo e a falta de apoio familiar para a educação. A implementação de programas educativos adaptados às necessidades locais e a melhoria das condições de infraestrutura são essenciais para combater o analfabetismo nesta região.")

pdf.image("Analfabetismo-Oeste.png", 20, 140, 170)

# ---- Quinta Página ---- #
pdf.add_page()
pdf.subtitulo("Comparação em desagregação em % de matrículas entre homens e mulheres")
pdf.paragrafo("\n")

pdf.paragrafo("A análise da desagregação das porcentagens de matrículas entre homens e mulheres é crucial para entender as disparidades e promover a igualdade de oportunidades educacionais.")

pdf.paragrafo("Em muitas instituições educacionais e sistemas de ensino ao redor do mundo, as taxas de matrícula podem variar significativamente entre os gêneros, refletindo diferentes níveis de acesso e participação.")

pdf.image("Comparacao-Desagregacao-homem-mulher.png", 10, 85, 180 )

# ---- Ultima página - Conclusão ---- #
pdf.add_page()
pdf.subtitulo("Conlusão")

pdf.paragrafo("\n")

pdf.paragrafo("A análise da educação no Brasil revela um cenário complexo e desafiador, onde a desigualdade continua a ser um obstáculo significativo para o desenvolvimento social e econômico. As disparidades regionais no analfabetismo destacam a necessidade urgente de políticas educacionais direcionadas. Regiões como o Norte e o Nordeste, que apresentam as maiores taxas de analfabetismo, requerem atenção especial para garantir que todos os brasileiros tenham acesso a uma educação básica de qualidade.")



pdf.paragrafo("Além disso, a desagregação das matrículas entre homens e mulheres expõe as desigualdades de gênero que persistem no sistema educacional. Embora tenha havido avanços significativos na equidade de gênero, ainda existem áreas em que os homens são mais prevalentes, especialmente em cursos técnicos e áreas STEM (Ciência, Tecnologia, Engenharia e Matemática). Por outro lado, as mulheres têm maior representação em áreas das ciências sociais e da saúde, refletindo tendências tradicionais que precisam ser desafiadas para promover uma participação mais equilibrada em todas as áreas de estudo.")

pdf.paragrafo("Essa análise deixa claro que, para alcançar uma educação verdadeiramente inclusiva e equitativa no Brasil, é fundamental implementar políticas públicas que abordem tanto as disparidades regionais quanto as de gênero. Investir em programas de alfabetização nas regiões mais carentes e promover a igualdade de acesso a todas as áreas de estudo para homens e mulheres são passos essenciais para superar as desigualdades existentes. Somente assim será possível construir um sistema educacional que ofereça oportunidades iguais para todos os cidadãos, independentemente de sua localização geográfica ou gênero.")

pdf.paragrafo("\n")
pdf.paragrafo("\n")
pdf.paragrafo("\n")


pdf.paragrafo("Feito por: Víctor Manuel Martínez Fuentes - São Paulo SP.")

pdf.output("Analise.pdf")

