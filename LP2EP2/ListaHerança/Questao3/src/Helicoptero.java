public class Helicoptero extends Veiculo implements Interface {
	private int helices;
	
	public Helicoptero(int velocidade, int numeroSerie, String modelo, double preco, int helices) {
		super(velocidade, numeroSerie, modelo, preco);
		this.helices = helices;
	}
	public boolean voar() {
		return true;
	}
}

