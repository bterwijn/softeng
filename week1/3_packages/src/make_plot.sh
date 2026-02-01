input="$1"
output="$2"
temp='temp_plot.py'

cp $input $temp
sed -i -e "s/plt.show()/plt.savefig(\"$output\")/g" $temp
python $temp
rm $temp
