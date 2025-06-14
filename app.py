from flask import Flask, render_template, request
from scipy.stats import pearsonr

app = Flask(__name__)
# angka = [1,3,2,3,4,5]


@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = None
    if request.method == 'POST':
        try:
            # Ambil data dari form dan ubah jadi list float
            x = list(map(float, request.form['x'].split(',')))
            y = list(map(float, request.form['y'].split(',')))

            # Pastikan panjang data sama
            if len(x) != len(y):
                hasil = '❌ Jumlah data X dan Y harus sama.'
            else:
                r, _ = pearsonr(x, y)
                r_tabel = 0.361  # Contoh nilai r tabel (df=8, α=0.05)
                status = '✅ Valid' if abs(r) > r_tabel else '❌ Tidak Valid'
                hasil = f'Koefisien korelasi (r) = {r:.3f} → {status}'
        except:
            hasil = '❌ Format input salah. Gunakan angka yang dipisahkan dengan koma (contoh: 20,22,25).'

    return render_template('index.html', hasil=hasil)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)

