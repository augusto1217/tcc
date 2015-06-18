/* Método utilizado zado para obter um determinado pacote e salva -lo 
* em um diretório
*/

public static boolean downloadFileFromURL(String urlString, File destination) { 
    
          FileOutputStream fos = null;
          ReadableByteChannel rbc = null;
            
        if(urlString.contains(" ")){
            urlString = urlString.replace(" ", "%20");
        }
        URL website;
        try {
            website = new URL(urlString);
        
            if(nomeArquivo == null) {
                return false;
            }
         
            nomeArquivo  = new String[1];
            String [] temp = urlString.split("/");
            nomeArquivo[0] = temp[temp.length-1];
            if(nomeArquivo[0].contains("%20")) {
                nomeArquivo[0] = nomeArquivo[0].replace("%20", "-");
            }
            if(nomeArquivo[0].contains("#")) {
                nomeArquivo = nomeArquivo[0].split("#");
            }
            
            rbc = Channels.newChannel(website.openStream());
            fos = new FileOutputStream(destination+File.separator+nomeArquivo[0]);
            fos.getChannel().transferFrom(rbc, 0, Long.MAX_VALUE);
            fos.close();
            
            if(fos != null){
                try {
                    fos.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                fos = null;
            }
            if(rbc != null){
                rbc = null;
            }
        } catch (MalformedURLException e1) {
            logger.error(e1.getMessage());
            return false;
        } catch (FileNotFoundException e1) {
            logger.error(e1.getMessage());
            return false;
        } catch (IOException e1) {
            logger.error(e1.getMessage());
            return false;
        }

        return true;
    }

