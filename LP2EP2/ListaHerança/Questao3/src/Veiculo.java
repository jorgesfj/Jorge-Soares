
public class Veiculo {
	 private int velocidade;
	 private int numeroSerie;
	 private String modelo;
	 private double preco;
	public int getVelocidade() {
		return velocidade;
	}
	public void setVelocidade(int velocidade) {
		this.velocidade = velocidade;
	}
	public int getNumeroSerie() {
		return numeroSerie;
	}
	public void setNumeroSerie(int numeroSerie) {
		this.numeroSerie = numeroSerie;
	}
	public String getModelo() {
		return modelo;
	}
	public void setModelo(String modelo) {
		this.modelo = modelo;
	}
	public double getPreco() {
		return preco;
	}
	public void setPreco(double preco) {
		this.preco = preco;
	}
	
	
	
	public Veiculo(int velocidade, int numeroSerie, String modelo, double preco) {
		super();
		this.velocidade = velocidade;
		this.numeroSerie = numeroSerie;
		this.modelo = modelo;
		this.preco = preco;
	}
	 
	public void acelerar(int velocidade) {
		this.velocidade += 10;
	} 
	
	public void frear(int velocidade) {
		this.velocidade -= 10;
	}
}
