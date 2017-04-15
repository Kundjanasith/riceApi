# echo "Start"
# touch ri.txt
# touch ri_ana.txt
# python Zx.py ri.png ri.txt ri_img.png
# python analyse.py ri.txt ri_ana.txt
# echo "Result : "
# python cat.py ri_ana.txt
# echo "Finish"

            # var_1 = ' x.txt'
            # var_2 = ' x_ana.txt'
            # var_3 = ' rice'+result
            # var_4 = ' '+result
            # os.system('bash django.sh'+var_1+var_2+var_3+var_4)

# echo "Start"
# echo "ri.txt" $1
# echo "ri_ana.txt" $2 

# echo "ri.png" $3
# echo "ri_img.png" $4

# python Zx.py $3 $1 $4
# cp rice/trash$4 rice/static/images$4
# python analyse.py $1 $2
# echo "Result : "
# python cat.py $2
# echo "Finish"

echo "Start"
cd backEnd
echo "res.png" 
python Zx.py res.png ri.txt res_img.png
python analyse.py ri.txt ri_ana.txt
python cat.py ri_ana.txt
cd ../getResult
python resultI.py
python resultT.py
echo "Finish"
