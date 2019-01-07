public class Aviao extends Veiculo implements Interface {
	private int numeroComissarios;
	
	public Aviao(int velocidade, int numeroSerie, String modelo, double preco, int numeroComissarios) {
		super(velocidade, numeroSerie, modelo, preco);
		this.numeroComissarios = numeroComissarios;
	}
	public boolean voar() {
		return true;
	}
}
