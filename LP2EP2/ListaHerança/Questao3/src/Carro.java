public class Carro extends Veiculo{
	private int numeroPassageiros;

	public Carro(int velocidade, int numeroSerie, String modelo, double preco, int numeroPassageiros) {
		super(velocidade, numeroSerie, modelo, preco);
		this.numeroPassageiros = numeroPassageiros;
	}

}
