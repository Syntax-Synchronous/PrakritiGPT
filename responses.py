import re

def message_probability(user_message, recognized_words, single_response = False, required_words = []):
    message_certainty = 0
    has_required_words = True
    
    for word in user_message:
        if word in recognized_words:
            message_certainty += 1
            
    per = float(message_certainty) / float(len(recognized_words))
    
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(per*100)
    else:
        return 0
    
def check_messages(message):
    highest_probability_list = {}
    
    def response(bot_response, list_of_words, single_response = False, required_words = []):
        nonlocal highest_probability_list
        highest_probability_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
        
    response('Hello! How can I help you today?', ['hello', 'hi', 'hey'], single_response=True)
    response('Ayurvedic treatments are a traditional system of medicine that originated in India thousands of years ago. Ayurveda is a holistic approach to health and well-being that focuses on achieving a balance between the body, mind, and spirit. The word "Ayurveda" is derived from the Sanskrit words "ayur," meaning life, and "veda," meaning knowledge, so it can be translated as the "science of life.\n\n\
Key principles and components of Ayurvedic treatments include:\n\n\
Herbal Remedies: Ayurvedic practitioners use a wide range of herbs and botanicals to create herbal remedies and supplements. These remedies are often customized to address specific health concerns or imbalances.\n\n\
Meditation and Mindfulness: Ayurveda emphasizes the importance of mental and emotional balance. Meditation and mindfulness techniques are often prescribed to reduce stress, promote mental clarity, and enhance overall well-being.\n\n\
Cleansing and Detoxification: Ayurvedic treatments include purification and detoxification practices known as "Panchakarma." These procedures are designed to eliminate toxins from the body and restore balance.\n\n\
Lifestyle Recommendations: Ayurvedic practitioners provide guidance on daily routines, sleep patterns, and lifestyle choices that align with an individual\'s dosha and promote optimal health.\n\n\
It\'s essential to note that Ayurveda is considered complementary or alternative medicine in many parts of the world, and its effectiveness can vary from person to person. If you are interested in Ayurvedic treatments, it\'s advisable to consult with a qualified Ayurvedic practitioner who can provide personalized recommendations based on your unique constitution and health concerns. Additionally, it\'s crucial to use Ayurvedic treatments in conjunction with conventional medical care, especially for serious or acute health conditions.', ['what', 'are', 'ayurvedic', 'treatments', 'ayurveda', 'diseases', 'help', 'treat'], required_words=['ayurvedic'])
    response('Ayurvedic medicine can have side effects, especially if not used properly or if the ingredients used are of poor quality. Some Ayurvedic remedies may interact with medications or cause allergic reactions in some individuals. It\'s important to consult with a qualified Ayurvedic practitioner and inform them of any existing health conditions or medications you are taking to minimize potential side effects and ensure safe use.', ['does', 'ayurveda', 'ayurvedic', 'medicine', 'have', 'side', 'effects'], required_words=['ayurvedic'])
    response('Ayurveda is not considered a primary or standalone treatment for cancer. While Ayurvedic practices may be used as complementary or supportive therapies to help manage the side effects of cancer treatments or to improve overall well-being during cancer care, they should not be used as a sole treatment for cancer. Cancer is a complex disease that typically requires conventional medical treatments such as surgery, chemotherapy, radiation therapy, immunotherapy, and targeted therapy.\n\n\
However, some people may choose to incorporate Ayurvedic practices into their overall wellness routine while undergoing cancer treatment. Ayurvedic treatments and recommendations may focus on dietary modifications, herbal supplements, yoga, meditation, and stress reduction techniques to support the individual\'s general health and quality of life during cancer treatment.\n\n\
It is crucial for anyone diagnosed with cancer to consult with a team of healthcare professionals, including oncologists and specialists, to determine the most appropriate and evidence-based treatment plan for their specific type and stage of cancer. These experts can provide guidance on integrating complementary therapies like Ayurveda safely into the overall cancer care plan.', ['is', 'there', 'ayurvedic', 'treatment', 'for', 'cancer'], required_words=['cancer'])
    response('Ayurvedic treatment for arthritis is a holistic approach that seeks to alleviate pain, reduce inflammation, and improve joint function. It encompasses a range of therapies and lifestyle modifications tailored to the individual\'s dosha constitution and the specific type of arthritis they have.\n\n\
Dietary Modifications: Ayurveda places significant emphasis on the role of diet in managing arthritis. Depending on the person\'s dosha type, an Ayurvedic practitioner may recommend specific foods to pacify aggravated doshas and reduce inflammation. Anti-inflammatory foods such as turmeric, ginger, and green leafy vegetables are often encouraged, while processed, spicy, and fried foods should be avoided.\n\n\
Herbal Remedies: Ayurvedic herbs and supplements play a crucial role in arthritis management. Some commonly used herbs for arthritis include turmeric (known for its anti-inflammatory properties), ginger, Boswellia, Ashwagandha, and Guggul. These herbs can help reduce pain and inflammation in the joints.\n\n\
Panchakarma: Panchakarma, a set of detoxification and cleansing therapies, may be recommended to remove toxins from the body. These therapies aim to reduce inflammation and improve joint mobility.\n\n\
Yoga and Gentle Exercise: Customized yoga poses and gentle exercises are designed to increase joint flexibility and reduce muscle tension. It\'s essential to avoid strenuous activities that can exacerbate arthritis symptoms.\n\n\
Meditation and Stress Reduction: Stress can worsen arthritis symptoms. Ayurveda promotes meditation and relaxation techniques to manage stress and promote overall well-being.\n\n\
Individualized treatment plans are essential in Ayurveda, as each person\'s constitution and arthritis condition may vary. It is advisable to work closely with a qualified Ayurvedic practitioner who can assess your specific needs and create a personalized treatment strategy.', ['what', 'is', 'the', 'ayurvedic', 'treatment', 'for', 'arthritis'], required_words= ['arthritis'])
    response('Ayurveda is believed to have evolved over thousands of years in ancient India, and it does not have a single attributed founder. Instead, Ayurveda is considered a body of knowledge that developed through the contributions of many ancient scholars and practitioners. Some of the foundational texts of Ayurveda, known as the "Vedas," particularly the "Rigveda" and the "Atharvaveda," contain early references to healing practices and herbal remedies.\n\n\
One of the most influential texts in Ayurveda is the "Charaka Samhita," attributed to the sage Charaka, who is often regarded as one of the founding figures of Ayurveda. Another significant text is the "Sushruta Samhita," attributed to the sage Sushruta, which focuses on surgical techniques and is particularly relevant to Ayurvedic surgery.\n\n\
While Charaka and Sushruta are prominent figures associated with Ayurveda, it\'s important to recognize that Ayurveda\'s development involved the contributions of numerous scholars, sages, and practitioners over centuries. The knowledge and practices of Ayurveda were traditionally passed down through oral tradition and written texts, making it a collective body of wisdom rather than the creation of a single individual.', ['who', 'created', 'ayurveda', 'creator', 'maker', 'person', 'individual'], required_words=['who', 'ayurveda'])
    response('Ayurvedic medicine is a traditional system of health care that originated in India about 3,000 years ago. It is derived from the Sanskrit words ayur (life) and veda (science or knowledge). Ayurveda is widely practiced in parts of Asia, especially in India and Nepal, where around 80% of the population report using it. Ayurveda has both preventive and curative aspects, and it adapts to the personal needs of each patient. Ayurveda uses herbal medicines, special diets, meditation, yoga, massage, and other therapies to promote health and well-being.\n\n\
        While Ayurveda originated in ancient India, it has gained recognition and popularity worldwide as a complementary and alternative system of medicine. In modern times, Ayurvedic practices, remedies, and therapies have been adapted and integrated into healthcare systems in many countries. However, it\'s important to consult with qualified Ayurvedic practitioners to ensure the safe and effective use of Ayurvedic treatments.', ['where', 'does', 'did', 'ayurveda', 'medicine', 'come', 'from', 'originate'], required_words=['where'])
    response('Ayurveda is a holistic system of medicine that originated in India and aims to balance the body, mind, and spirit. Ayurveda believes that every person has a unique constitution, or prakriti, based on the combination of three fundamental energies, or doshas. These are vata (air and space), pitta (fire and water), and kapha (earth and water) . Ayurveda diagnoses and treats diseases by identifying the imbalance of doshas and restoring harmony through natural remedies and lifestyle changes. Ayurveda also emphasizes the importance of dharma (purpose), artha (wealth), kama (pleasure), and moksha (liberation) as the four goals of human life . Ayurveda is not only a system of medicine, but also a way of living in harmony with nature and oneself.', ['what', 'is', 'ayurveda', 'definition', 'root'], required_words=['ayurveda'])
    response('The 5 Prana Vayus are the five types of vital energy that flow through the body and mind. They are:\n\n\
Prana-Vayu: The energy of intake, inspiration, and forward movement. It is located in the chest and head, and it nourishes the brain, eyes, and senses. It is associated with the heart chakra and the element of air\n\n\
Apana-Vayu: The energy of elimination, downward and outward movement. It is located in the pelvis, and it regulates the excretion of waste and toxins. It is associated with the root chakra and the element of earth\n\n\
Samana-Vayu: The energy of assimilation, discernment, and inner absorption. It is located in the navel, and it balances the digestion of food, thoughts, and emotions. It is associated with the solar plexus chakra and the element of fire\n\n\
Udana-Vayu: The energy of growth, speech, expression, and upward movement. It is located in the throat, and it supports the development of the body and mind. It is also responsible for the transition between states of consciousness. It is associated with the throat chakra and the element of space\n\n\
Vyana-Vayu: The energy of circulation, expansiveness, and pervasiveness. It is located throughout the whole body, and it distributes prana to every cell and organ. It also connects us to our surroundings and other beings. It is associated with all the chakras and all the elements\n\n\
These five Vayus work together to create harmony in our physical, mental, and spiritual health. By becoming aware of them and practicing yoga techniques that enhance their flow, we can improve our well-being and achieve higher states of awareness.', ['what', 'are', 'the', '5', 'five', 'prana', 'vayus'], required_words=['vayus'])
    response('The effectiveness of Ayurveda depends on various factors, such as the type and severity of the condition, the individual constitution of the person, the quality and safety of the Ayurvedic products, and the expertise of the practitioner. Ayurveda is considered a complementary health approach in the United States, and research on its effectiveness is limited. However, some studies have shown that Ayurvedic treatments may have some benefit for certain conditions, such as:\n\n\
Anxiety: A 2017 systematic review of 10 randomized controlled trials found that Ayurvedic interventions, such as herbal medicines, yoga, and meditation, were more effective than placebo or no intervention in reducing anxiety symptoms.\n\n\
Brain function: A 2018 randomized controlled trial of 60 healthy adults found that an Ayurvedic herbal formulation called Brahmi improved cognitive performance, attention, and working memory compared to placebo.\n\n\
High cholesterol: A 2016 systematic review of 17 randomized controlled trials found that Ayurvedic herbal medicines were more effective than placebo or conventional drugs in lowering total cholesterol, LDL cholesterol, and triglycerides.\n\n\
Osteoarthritis: A 2013 randomized controlled trial of 440 people with knee osteoarthritis found that two Ayurvedic formulations of plant extracts were as effective as glucosamine sulfate and celecoxib in reducing pain and improving function.\n\n\
These are some examples of the potential benefits of Ayurveda for certain health issues. However, more rigorous and larger-scale studies are needed to confirm the effectiveness and safety of Ayurveda for various conditions. It is important to consult with your doctor before using any Ayurvedic products or therapies, as they may interact with other medications or cause adverse effects. You should also seek qualified and reputable Ayurvedic practitioners who have adequate training and experience in this field.', ['how', 'is', 'ayurveda', 'effective', 'beneficial', 'benefits'], required_words=['effective'])

    best_match = max(highest_probability_list, key=highest_probability_list.get)
    print(highest_probability_list)
    
    return best_match

def get_response(message: str) -> str:
    p_message = re.split(r'\s+|[,;?!.-]\s*', message.lower())
    response = check_messages(p_message)
    print(len(response))
    return response


    
    

    
