/** Armazena o producto no banco de dados. */

public void save() throws Exception {
     // Verifica propriedades
     if (this.getName() == null) {
         throw new Exception("Falta o nome");
     } else if (this.getDescription() == null) {
         throw new Exception("Falta a descrição");
     }
     this.getDatabase().save(this);
}
