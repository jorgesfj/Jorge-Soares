public class Main {
	public static void main(String[] args) {
		
		Gerente g1 = new Gerente("Joao", 5000, "B");
		System.out.println(g1.toString(g1.getNome(),g1.getSalario(),g1.getDepartamento()));
		
		
		
		Vendedor v1 = new Vendedor("Carlos",980,0.25);
		System.out.println(v1.toString("Carlos",980,0.25));
		}
	
}
