/** Armazena o produto no banco de dados. */
 
public void save() throws Exception {
     this.checkProperties();
     this.getDatabase().save(this);
 } 

/** Verifica as propriedades do produto. */
 
private void checkProperties() throws Exception {
     if (this.getName() == null) {
         throw new Exception("Falta nome do produto.");
     } else if (this.getDescription() == null) {
         throw new Exception("Falta a descrição do produto.");
     }
}
