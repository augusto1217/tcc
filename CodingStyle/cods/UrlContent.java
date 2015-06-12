/*
* Método utilizado para receber um endereço eletrônico e  executar o
* processo de transferência do mesmo.
*/

public class UrlContent implements Runnable {
	
	private static Logger logger = Logger.getLogger(UrlContent.class);
	static String []  nomeArquivo = null;
	private static boolean status = false;
	
	public UrlContent() {
		
	}
	
	public static void down(){
		PrintWriter pw = null;
		File arquivoUrlHtml = null;
		File errorFile = null;
		FileReader fr = null;
		BufferedReader br1 = null;
		String link = null;
    	try {
    		arquivoUrlHtml = new File("file/write.txt");
    		errorFile = new File("file/error.txt");

    		fr = new FileReader(arquivoUrlHtml);
    		br1 = new BufferedReader(fr);
    		pw = new PrintWriter(new FileWriter(errorFile));
			
			while (br1.ready()) {
				link = br1.readLine();
				if(!executaDownFile(link)){
					pw.append(link + "\r\n");
					pw.flush();
				}
			}
			
			br1.close();
			fr.close();
			
			if(pw != null) {
				pw.close();
				pw = null;
			}
			if(br1 != null) {
				br1 = null;
			}
			if(fr != null) {
				fr = null;
			}
			if(arquivoUrlHtml != null) {
				arquivoUrlHtml = null;
			}
			
		} catch (IOException e) {
			pw.append(link + "\r\n");
			pw.flush();
			logger.error(e.getMessage());
			return;
		} 
    }
	
	private static boolean executaDownFile(String links) {
		
		File path = null;;
		
		if(isWindows()) {
			path = new File("./arquivos");
		} else {
			path = new File("/arquivos");
		}
		
		if(!path.exists()){
			path.mkdir();
		}
		
		String [] words = new String[100000];
			
		URL url;
		try {
			url = new URL(links);
			
		
			URLConnection conn = url.openConnection();
			InputStream in = conn.getInputStream();
			BufferedReader br = new BufferedReader(new InputStreamReader(in));
			String linhaHtml;
			int count = 0;
			nomeArquivo = null;
			while ((linhaHtml = br.readLine()) != null) {
				words[count] = linhaHtml;
				if(linhaHtml.contains(".zip") 
						|| linhaHtml.contains(".tar.gz") 
						|| linhaHtml.contains(".tgz") 
						|| linhaHtml.contains(".whl")
						|| linhaHtml.contains(".bz2")
						|| linhaHtml.contains(".egg")){
					
					if(linhaHtml.contains("master.zip")){
						return false;
					}
					
					if(linhaHtml.contains("bitbucket")){
						return false;
					}
					
					if(linhaHtml.contains("\"")){
						nomeArquivo = linhaHtml.split("\"");
						if(nomeArquivo.length > 5) {
							nomeArquivo[0] = nomeArquivo[5].trim();
							break;
						}
					}
					
					nomeArquivo = linhaHtml.split("<a href=\"https:");
					if(nomeArquivo.length > 1){
						if(nomeArquivo[1].contains("</a")){
							nomeArquivo = nomeArquivo[1].split("</a");
							if(nomeArquivo[0].contains(">")){
								nomeArquivo = nomeArquivo[0].split(">");
							}
							if(nomeArquivo[0].contains("?")){
								nomeArquivo = nomeArquivo[0].split("\\?");
							}
							nomeArquivo[0] = "https:"+nomeArquivo[0];
							if(fileExist(nomeArquivo[0])){
								return true;
							}
							status = downloadFileFromURL(nomeArquivo[0].replace("\"", ""),path);
							if(!status){
								return false;
							} else {
								return true;
							}
						}else {
							nomeArquivo = nomeArquivo[1].split("#");
							nomeArquivo[0] = "https:"+nomeArquivo[0].trim();
						}
						break;
					} else {
						nomeArquivo = nomeArquivo[0].split("#");
						if(nomeArquivo[0].contains("<a href=\"http:")) {
							if(nomeArquivo.length >= 2) {
								String tmp = nomeArquivo[2];
								String [] tmpArray = tmp.split("</a");
								nomeArquivo = nomeArquivo[0].split("<a href=\"http:");
								nomeArquivo[0] = "http:"+nomeArquivo[1]+"#"+tmpArray[0];
							} else {
								nomeArquivo = nomeArquivo[0].split("<a href=\"http:");
								if(nomeArquivo[1].contains("</a")){
									nomeArquivo = nomeArquivo[1].split("</a");
									nomeArquivo[0] = "http:"+nomeArquivo[0];
									if(nomeArquivo[0].contains(">")){
										nomeArquivo = nomeArquivo[0].split(">");
									}
									if(nomeArquivo[0].contains("?")){
										nomeArquivo = nomeArquivo[0].split("\\?");
									}
									if(nomeArquivo[0].contains("\"")){
										nomeArquivo = nomeArquivo[0].split("\"");
									}
									if(fileExist(nomeArquivo[0])){
										return true;
									}
									status = downloadFileFromURL(nomeArquivo[0].replace("\"", ""),path);
									if(!status){
										return false;
									} else {
										return true;
									}
								}else {
									nomeArquivo[0] = "http:"+nomeArquivo[1];
								}
							}
						} else {
							nomeArquivo[0] = "https:"+nomeArquivo[0].trim();
						}
						break;
					}
				}
				count++;
			}
			
			if(nomeArquivo == null) {
				return false;
			}
			
			String[] nomeArquivoExiste = nomeArquivo[0].split("/");
			if(nomeArquivoExiste.length >= 8) {
				System.out.println(links);
				if(fileExist(nomeArquivoExiste[7])) {
					return true;
				}
			} else {
				return false;
			}
			
			if(nomeArquivo[0].contains("https") || nomeArquivo[0].contains("http")){
				status = downloadFileFromURL(nomeArquivo[0].replace("\"", ""),path);
			} else {
				status = downloadFileFromURL("https" + nomeArquivo[0].replace("\"", ""),path);
			}
			if(!status){
				return false;
			}
		} catch (MalformedURLException e) {
			logger.error(e.getMessage());
			return false;
		} catch (IOException e) {
			logger.error(e.getMessage());
			return false;
		}
		
		return true;
	}
}
