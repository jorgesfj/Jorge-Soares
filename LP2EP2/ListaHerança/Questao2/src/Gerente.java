public class Gerente extends Empregado {
	
	private String departamento;
	
	public Gerente(String nome, float salario, String departamento) {
		super(nome, salario);
		this.departamento = departamento;
	}

	

	public String getDepartamento() {
		return departamento;
	}

	public void setDepartamento(String departamento) {
		this.departamento = departamento;
	}

	public String toString(String nome, float salario, String departamento) {
		return "O funcion�rio: " +nome+ "E departamento:  "+departamento+"Tem salario de : " + salario;
	}
}
