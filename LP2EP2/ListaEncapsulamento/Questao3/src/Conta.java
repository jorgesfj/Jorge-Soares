
public class Conta {
	private int numero;
	private double saldo;
	
	
	public void deposito(int numero) {
		if (this.numero == numero){
		}
	}
	
	public boolean saque(int numero,double valor) {
			if (this.numero == numero) {
				if (valor<=this.saldo) {
					this.saldo -= valor;
					return true;
				}else {
					return false;
				}
			}else {
				return false;
			}
			
	}
}
