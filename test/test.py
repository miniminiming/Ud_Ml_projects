from nltk.corpus import stopwords
import nltk

# nltk.download()
#
# sw = stopwords.words("english")
#
# print "stop words length",len(sw)

text = "i am you father , ha ha ha"
text.replace("am","")
print text

text_words = text.split(" ")
delete_words=["am"]
text = " ".join([word for word in text_words if word not in delete_words])
print text

text = "i am you father , ha ha ha"
text = text.replace("am","")
print text