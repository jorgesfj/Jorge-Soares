public class Animal {
	private String descricao;
	private String nome;
	private String tipo;
	
	
	public String getTipo() {
		return tipo;
	}
	public void setTipo(String tipo) {
		this.tipo = tipo;
	}
	public String getDescricao() {
		return descricao;
	}
	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}
	public String getNome() {
		return nome +" é um animal";
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public void locomover() {
		
	}
	public void alimentar() {
		
	}
	
}
