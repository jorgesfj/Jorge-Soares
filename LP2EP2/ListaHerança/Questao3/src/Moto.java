public class Moto extends Veiculo{
	private boolean corrente;
	
	public Moto(int velocidade, int numeroSerie, String modelo, double preco, boolean corrente) {
		super(velocidade, numeroSerie, modelo, preco);
		this.corrente = corrente;
	}
}
