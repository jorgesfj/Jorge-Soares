public interface Relogio {
	void setHorario(double horario);
	double getHorario();
	void setHorarioAlarme(double horario);
	double getHorarioAlarme(double horario);
	boolean ligarAlarme();
	boolean desligarAlarme();
	void setVolumeRelogio(int vol);
	int getVolumeRelogio();
}
