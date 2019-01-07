public class Main {
	
	public static void main(String[]args) {
		
		Ingresso i1 = new Ingresso();
		i1.setValor(15);
		
		IngressoVIP iv1 = new IngressoVIP();
		iv1.setValor(15);
		iv1.setValorAdicional(10);
		
		
		System.out.println("O preço de um ingresso é de "+i1.toString(i1.getValor())+". E o preço de um"
				+ " ingresso VIP é de "+ iv1.toString(i1.getValor(),iv1.getValorAdicional()));
		
	}
}
