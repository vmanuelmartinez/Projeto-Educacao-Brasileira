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

pdf.output("Analise.pdf")