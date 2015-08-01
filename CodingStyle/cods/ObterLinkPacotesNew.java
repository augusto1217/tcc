import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;

/*
* Método utilizado para obter a url de um determinado pacote e salvá-lo 
* em um arquivo texto em um diretório
*/

public class ObterLinkPacotes {

	public static void main(String[] args) {
		ler();
	}

	private static void ler() {
		try {
			URL url = new URL("https://pypi.python.org/pypi?:action=index");
			BufferedReader br = new BufferedReader(new InputStreamReader(url.openStream()));
			String linha;
			String chaves[];
			while ((linha = br.readLine()) != null) {
				if (linha.contains("<td><a href=\"")) {
					chaves = linha.split("\"");
					if (chaves[1].contains(" ")) {
						chaves[1] = chaves[1].replace(" ", "%20");
					}
					criarArquivo("https://pypi.python.org" + chaves[1]);
				}
			}
			br.close();
		} catch (MalformedURLException excecao) {
			excecao.printStackTrace();
		} catch (IOException excecao) {
			excecao.printStackTrace();
		}
	}

	private static void criarArquivo(String texto) throws IOException {

		String caminho = "./file/write.txt";
		FileWriter arquivo = new FileWriter(caminho, true);
		BufferedWriter escreverArquivo = new BufferedWriter(arquivo);

		escreverArquivo.write(texto);
		escreverArquivo.newLine();
		escreverArquivo.flush();
		escreverArquivo.close();
		arquivo.close();
	}

}

