package com.listaheranca.questao5;

public class RadioRelogio implements Radio, Relogio {
	private String horario;
	private String despertar;
	private String horarioAlarme;
	private String emissora;
	private String tipoEmissora;
	private String volumeRadio;
	private String volumeRelogio;
	@Override
	public void setHorario(String horario) {
		this.horario = horario;
	}
	@Override
	public String getHorario() {
		return this.horario;
	}
	@Override
	public void setHorarioAlarme(String horario) {
		this.horario = horario;
	}
	@Override
	public String getHorarioAlarme() {
		return this.horarioAlarme;
	}
	@Override
	public void ligarAlarme() {
	}
	@Override
	public void desligarAlarme() {
	}
	@Override
	public void setVolumeRelogio(String volumeRelogio) {
		this.volumeRelogio = volumeRelogio;
	}
	@Override
	public String getVolumeRelogio() {
		return this.volumeRelogio;
	}
	@Override
	public void setEmissora(String Emissora, String tipoEmissora) {
		this.emissora = emissora;
		this.tipoEmissora = tipoEmissora;
	}
	@Override
	public String getEmissora() {
		return this.emissora;
	}
	@Override
	public String getTipoEmissora() {
		return this.tipoEmissora;
	}
	@Override
	public void setVolumeRadio(String volumeRadio) {
		this.volumeRadio = volumeRadio;
	}
	@Override
	public String getVolumeRadio() {
		return this.volumeRadio;
	}
	
	
}
