# Pythono3 code to rename multiple 
# files in a directory or folder 

# importing os module 
import os
import io
import frontmatter

from io import BytesIO
from frontmatter.default_handlers import TOMLHandler

slugs = ["evernote-reminder-vs-todoist-comparison",
        "cloud-notes-compare-2020",
        "all-because-a-lack-of-patience",
        "2020%E5%B9%B4%E6%97%A2%E9%A0%AD2%E5%80%8B%E6%9C%88%E7%9A%84%E7%94%9F%E6%B4%BB",
        "convert-matlab-matrix-to-ms-office-equation",
        "final-call-for-free-upgrade-to-windows-10",
        "a-glimpse-of-smart-logistics-development-in-china",
        "how-to-subscribe-a-site-not-supporting-rss-feed",
        "introduction-of-trello-for-project-management",
        "how-to-deal-with-angry",
        "instagram-uploader-gramblr-is-dead",
        "deep-thinking-on-the-flat-earth-critique",
        "how-to-develop-a-unicorn-company",
        "does-gramblr-uploader-die",
        "working-or-starting-a-business",
        "tcm-treatments-for-sore-throat",
        "from-doctoral-student-to-no-name",
        "winlaunch-osx-launchpadl-for-windows",
        "asana-vs-monday-comparison-2019",
        "you-are-your-best-lover",
        "google-keep-as-a-free-ocr-app",
        "effective-learning-tips-to-avoid-procrastination",
        "pay-attention-to-procrastination-causing-mental-illnesse",
        "build-positive-life-with-todoist",
        "solve-duplex-scanning-with-naps2",
        "amazon-enforced-main-image-policy",
        "you-dont-have-to-change-yourself-for-others",
        "five-things-you-should-know-when-feel-depressions",
        "lets-understand-more-about-bipolar-disorder",
        "rescuing-sub-health-patching-life-short-planks",
        "solve-teamviewer-commercial-use-suspected",
        "11-energy-boosting-food-for-health",
        "4-dimensions-forming-your-innovative-power",
        "introduction-of-sprint-project-management",
        "watch-out-for-nephritis-2-learn-more-medical-knowledge",
        "zero-cost-startup-with-teespring",
        "use-pixlr-editor-on-google-drive-to-edit-photo-online",
        "watch-out-for-nephritis-1-simple-self-diagnosis",
        "welcome-to-join-our-amazon-seller-facebook-group",
        "15-ways-to-talk-phd-that-sours-any-research-students",
        "review-li-ka-shing-mindset-for-growth-success",
        "email-marketing-element-1",
        "why-i-do-not-install-whatsapp-business",
        "tcm-said-cough-is-a-multiple-organ-illness",
        "gentle-makes-wealth-happy-new-year",
        "happy-dog-year-site-update-news",
        "financial-condition-limits-research-students-freedom",
        "how-to-setup-business-emails-with-zoho-mail-free-hosting",
        "important-to-think-big",
        "2017-annual-review-%E8%B2%BC%E5%9C%B0-%E9%9B%A2%E5%9C%B0",
        "what-do-i-want-in-my-life-during-depression",
        "10-benefits-from-planting-for-personal-development",
        "spoon-feeding-education-case-study-of-green-policy",
        "custom-plan-of-get-out-of-comfort-zone-1-personality-ana",
        "get-out-of-your-comfort-zone",
        "%E6%90%AC%E9%81%B7%E4%B8%AD",
        "why-winning-at-starting-line-ruins-our-life",
        "neck-pain-and-negative-moods",
        "effect-of-gut-bacteria-on-mental-health",
        "%E7%B2%BE%E7%A5%9E%E6%AC%A0%E4%BD%B3-%E6%AA%A2%E6%9F%A5%E4%BD%A0%E7%9A%84%E8%85%B3%E5%BA%95%E9%A1%8F%E8%89%B2",
        "worth-of-pleasure-with-infographic",
        "depression-and-3-precautions",
        "anxiety-and-3-reasons",
        "downshifting-relax-and-thinksgiving",
        "resolve-your-regret-by-writing",
        "regret-and-lost-of-tarareba-group",
        "get-instagram-free-like-using-gramblr-uploader",
        "3-reasons-of-opposite-development-of-plover-cove-reservo",
        "custom-evernote-text-highlight-shortcut-key",
        "nihonbyou-the-japan-syndrome",
        "microsoft-trade-in-hong-kong"]

postid = ["613551096372281344",
        "611808591193702400",
        "190912308823",
        "190905777158",
        "190306102953",
        "189713285693",
        "188919190933",
        "175430205233",
        "188585014873",
        "188120582123",
        "186691940763",
        "186559714563",
        "186351537463",
        "185920962238",
        "185676327238",
        "185491482758",
        "185154013813",
        "182823138243",
        "181920810493",
        "166221532353",
        "180434421358",
        "180238485643",
        "179004869008",
        "178534197203",
        "178313769748",
        "178040319138",
        "177685390898",
        "177129967128",
        "176770591678",
        "176584980633",
        "176549914983",
        "175299368035",
        "174939074693",
        "174462999633",
        "173831681003",
        "173991626203",
        "173836857302",
        "173664994648",
        "173247032813",
        "172955291233",
        "168815289098",
        "171692748288",
        "171518823643",
        "171409577053",
        "166221532088",
        "170940953278",
        "170718051943",
        "169679139013",
        "169418620658",
        "169108900148",
        "166221543018",
        "168351090068",
        "167906194108",
        "167662983553",
        "167409002198",
        "166942060588",
        "166221544358",
        "166221544103",
        "166221543663",
        "166221543368",
        "166221542498",
        "166221542238",
        "166221541698",
        "166221541378",
        "166221541163",
        "166221540808",
        "166221540398",
        "166221540103",
        "166221539713",
        "166221539508",
        "166221539128"]

postpath = [
        "166221541163/resolve-your-regret-by-writing",
        "166221540808/regret-and-lost-of-tarareba-group",
        "166221540398/get-instagram-free-like-using-gramblr-uploader",
        "166221540103/3-reasons-of-opposite-development-of-plover-cove-reservo",
        "166221539713/custom-evernote-text-highlight-shortcut-key",
        "166221539508/nihonbyou-the-japan-syndrome",
        "166221538713/philosopher-president-emmanuel-macron",
        "166221539128/microsoft-trade-in-hong-kong"
        ]

# Function to rename multiple files 
def main(): 
    
	for count, filename in enumerate(os.listdir(".")): 
		if(count < len(postid)):
			dst = filename[0:11] + slugs[-count-1] + ".html"
			#dst = filename[0:14] + ".html"
			src = filename 
			#dst ='xyz'+ dst 
			#print(filename[0:11])
			#print("{}/{}".format(postid[-count], slugs[-count]))
			# rename() function will 
			# rename all the files 
			os.rename(src, dst)



def changeSlug():
        for count, filename in enumerate(os.listdir(".")):
                if (filename!='rename.py'):
                        with io.open(filename, 'r' ,encoding='UTF-8') as f:
                                post = frontmatter.loads(f.read())

                                
                                print(post.get('slug'))
                                post['slug'] = postpath[-count-1]
                                print(post.get('slug'))
                                post_str = frontmatter.dumps(post)
                                f.close()

                                with io.open(filename, 'w' ,encoding='UTF-8') as f:
                                        f.write(post_str)

# Driver Code 
if __name__ == '__main__': 
	
	# Calling main() function 
        changeSlug() 
