public class RadioRelogio implements Radio,Relogio{
	private double horario;
	private double despertar;
	private double horarioAlarme;
	private String Emissora;
	private String tipoEmissora;
	private int volumeRadio;
	private int volumeRelogio;
	
	@Override
	public void setHorario(double horario) {
		this.horario = horario;
	}

	@Override
	public double getHorario() {
		return horario;
	}

	@Override
	public void setHorarioAlarme(double horarioAlarme) {
		this.horarioAlarme = horarioAlarme;
	}

	@Override
	public double getHorarioAlarme(double horario) {
		return horarioAlarme;
		
	}

	@Override
	public boolean ligarAlarme() {
		return true;
	}

	@Override
	public boolean desligarAlarme() {
		return false;
	}

	@Override
	public void setVolumeRelogio(int volumeRelogio) {
		this.volumeRelogio = volumeRelogio;
		
	}

	@Override
	public int getVolumeRelogio() {
		return volumeRelogio;
	}

	@Override
	public void setEmissora(String Emissora, String tipoEmissora) {
		this.Emissora = tipoEmissora;
	}

	@Override
	public String getEmissora() {
		return Emissora;
	}

	@Override
	public String getTipoEmissora() {
		return tipoEmissora;
	}

	@Override
	public void setVolumeRadio(int volumeRadio) {
		this.volumeRadio = volumeRadio;
	}
	

}
