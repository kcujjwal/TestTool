from cmath import acosh, nan
from tkinter.ttk import Style
from turtle import color
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns
from plotly.subplots import make_subplots
import plotly.graph_objects as go

incomeCat=pd.read_csv("IncomeCat.csv")

flags = {
   'Afghanistan': 'af', 'Albania': 'al', 'Algeria': 'dz', 'American Samoa': 'as', 'Andorra': 'ad', 'Angola': 'ao', 'Anguilla': 'ai', 'Antarctica': 'aq', 'Antigua and Barbuda': 'ag', 'Argentina': 'ar', 'Armenia': 'am', 'Aruba': 'aw', 'Australia': 'au', 'Austria': 'at', 'Azerbaijan': 'az', 'Bahamas': 'bs', 'Bahrain': 'bh', 'Bangladesh': 'bd', 'Barbados': 'bb', 'Belarus': 'by', 'Belgium': 'be', 'Belize': 'bz', 'Benin': 'bj', 'Bermuda': 'bm', 'Bhutan': 'bt', 'Bolivia, Plurinational State of': 'bo', 'Bolivia': 'bo', 'Bosnia and Herzegovina': 'ba', 'Botswana': 'bw', 'Bouvet Island': 'bv', 'Brazil': 'br', 'British Indian Ocean Territory': 'io', 'Brunei Darussalam': 'bn', 'Brunei': 'bn', 'Bulgaria': 'bg', 'Burkina Faso': 'bf', 'Burundi': 'bi', 'Cambodia': 'kh', 'Cameroon': 'cm', 'Canada': 'ca', 'Cape Verde': 'cv', 'Cayman Islands': 'ky', 'Central African Republic': 'cf', 'Chad': 'td', 'Chile': 'cl', 'China': 'cn', 'Christmas Island': 'cx', 'Cocos (Keeling) Islands': 'cc', 'Colombia': 'co', 'Comoros': 'km', 'Congo': 'cg', 'DR Congo':'cd','Congo, the Democratic Republic of the': 'cd', 'Cook Islands': 'ck', 'Costa Rica': 'cr', "Côte d'Ivoire": 'ci', 'Ivory Coast': 'ci', 'Croatia': 'hr', 'Cuba': 'cu', 'Cyprus': 'cy', 'Czech Republic': 'cz', 'Denmark': 'dk', 'Djibouti': 'dj', 'Dominica': 'dm', 'Dominican Republic': 'do', 'Ecuador': 'ec', 'Egypt': 'eg', 'El Salvador': 'sv', 'Equatorial Guinea': 'gq', 'Eritrea': 'er', 'Estonia': 'ee', 'Ethiopia': 'et', 'Falkland Islands (Malvinas)': 'fk', 'Faroe Islands': 'fo', 'Fiji': 'fj', 'Finland': 'fi', 'France': 'fr', 'French Guiana': 'gf', 'French Polynesia': 'pf', 'French Southern Territories': 'tf', 'Gabon': 'ga', 'Gambia': 'gm', 'Georgia': 'ge', 'Germany': 'de', 'Ghana': 'gh', 'Gibraltar': 'gi', 'Greece': 'gr', 'Greenland': 'gl', 'Grenada': 'gd', 'Guadeloupe': 'gp', 'Guam': 'gu', 'Guatemala': 'gt', 'Guernsey': 'gg', 'Guinea': 'gn', 'Guinea-Bissau': 'gw', 'Guyana': 'gy', 'Haiti': 'ht', 'Heard Island and McDonald Islands': 'hm', 'Holy See (Vatican City State)': 'va', 'Honduras': 'hn', 'Hong Kong': 'hk', 'Hungary': 'hu', 'Iceland': 'is', 'India': 'in', 'Indonesia': 'id', 'Iran, Islamic Republic of': 'ir', 'Iraq': 'iq', 'Ireland': 'ie', 'Isle of Man': 'im', 'Israel': 'il', 'Italy': 'it', 'Jamaica': 'jm', 'Japan': 'jp', 'Jersey': 'je', 'Jordan': 'jo', 'Kazakhstan': 'kz', 'Kenya': 'ke', 'Kiribati': 'ki', "Korea, Democratic People's Republic of": 'kp', 'Korea, Republic of': 'kr', 'South Korea': 'kr', 'Kuwait': 'kw', 'Kyrgyzstan': 'kg', "Lao People's Democratic Republic": 'la', 'Latvia': 'lv', 'Lebanon': 'lb', 'Lesotho': 'ls', 'Liberia': 'lr', 'Libyan Arab Jamahiriya': 'ly', 'Libya': 'ly', 'Liechtenstein': 'li', 'Lithuania': 'lt', 'Luxembourg': 'lu', 'Macao': 'mo', 'Macedonia, the former Yugoslav Republic of': 'mk', 'Madagascar': 'mg', 'Malawi': 'mw', 'Malaysia': 'my', 'Maldives': 'mv', 'Mali': 'ml', 'Malta': 'mt', 'Marshall Islands': 'mh', 'Martinique': 'mq', 'Mauritania': 'mr', 'Mauritius': 'mu', 'Mayotte': 'yt', 'Mexico': 'mx', 'Micronesia, Federated States of': 'fm', 'Moldova, Republic of': 'md', 'Monaco': 'mc', 'Mongolia': 'mn', 'Montenegro': 'me', 'Montserrat': 'ms', 'Morocco': 'ma', 'Mozambique': 'mz', 'Myanmar': 'mm', 'Burma': 'mm', 'Namibia': 'na', 'Nauru': 'nr', 'Nepal': 'np', 'Netherlands': 'nl', 'Netherlands Antilles': 'an', 'New Caledonia': 'nc', 'New Zealand': 'nz', 'Nicaragua': 'ni', 'Niger': 'ne', 'Nigeria': 'ng', 'Niue': 'nu', 'Norfolk Island': 'nf', 'Northern Mariana Islands': 'mp', 'Norway': 'no', 'Oman': 'om', 'Pakistan': 'pk', 'Palau': 'pw', 'Palestinian Territory, Occupied': 'ps', 'Panama': 'pa', 'Papua New Guinea': 'pg', 'Paraguay': 'py', 'Peru': 'pe', 'Philippines': 'ph', 'Pitcairn': 'pn', 'Poland': 'pl', 'Portugal': 'pt', 'Puerto Rico': 'pr', 'Qatar': 'qa', 'Réunion': 're', 'Romania': 'ro', 'Russian Federation': 'ru', 'Russia': 'ru', 'Rwanda': 'rw', 'Saint Helena, Ascension and Tristan da Cunha': 'sh', 'Saint Kitts and Nevis': 'kn', 'Saint Lucia': 'lc', 'Saint Pierre and Miquelon': 'pm', 'Saint Vincent and the Grenadines': 'vc', 'Saint Vincent & the Grenadines': 'vc', 'St. Vincent and the Grenadines': 'vc', 'Samoa': 'ws', 'San Marino': 'sm', 'Sao Tome and Principe': 'st', 'Saudi Arabia': 'sa', 'Senegal': 'sn', 'Serbia': 'rs', 'Seychelles': 'sc', 'Sierra Leone': 'sl', 'Singapore': 'sg', 'Slovakia': 'sk', 'Slovenia': 'si', 'Solomon Islands': 'sb', 'Somalia': 'so', 'South Africa': 'za', 'South Georgia and the South Sandwich Islands': 'gs', 'South Sudan': 'ss', 'Spain': 'es', 'Sri Lanka': 'lk', 'Sudan': 'sd', 'Suriname': 'sr', 'Svalbard and Jan Mayen': 'sj', 'Swaziland': 'sz', 'Sweden': 'se', 'Switzerland': 'ch', 'Syrian Arab Republic': 'sy', 'Taiwan, Province of China': 'tw', 'Taiwan': 'tw', 'Tajikistan': 'tj', 'Tanzania': 'tz', 'Thailand': 'th', 'Timor-Leste': 'tl', 'Togo': 'tg', 'Tokelau': 'tk', 'Tonga': 'to', 'Trinidad and Tobago': 'tt', 'Tunisia': 'tn', 'Turkey': 'tr', 'Turkmenistan': 'tm', 'Turks and Caicos Islands': 'tc', 'Tuvalu': 'tv', 'Uganda': 'ug', 'Ukraine': 'ua', 'United Arab Emirates': 'ae', 'United Kingdom': 'gb', 'United States': 'us', 'United States of America':'us','United States Minor Outlying Islands': 'um', 'Uruguay': 'uy', 'Uzbekistan': 'uz', 'Vanuatu': 'vu', 'Venezuela, Bolivarian Republic of': 've', 'Venezuela': 've', 'Viet Nam': 'vn', 'Vietnam': 'vn', 'Virgin Islands, British': 'vg', 'Virgin Islands, U.S.': 'vi', 'Wallis and Futuna': 'wf', 'Western Sahara': 'eh', 'Yemen': 'ye', 'Zambia': 'zm', 'Zimbabwe': 'zw'
   }


# capitals = ['Score','natural','human','social','financial','manufactured']
# capitals = ['Food Systems Resilience Score','Natural','Human','Social','Financial','Manufactured']
capitals = ['Food Systems Resilience Score','Natural Capital','Human Capital','Social Capital','Financial Capital','Manufactured Capital']
# capitalHeaders = {
#     'Food Systems Resilience Score':'Food Systems Resilience Score',
#     'Natural': 'Natural Capital',
#     'Human': 'Human Capital',
#     'Social': 'Social Capital',
#     'Financial': 'Financial Capital',
#     'Manufactured': 'Manufactured Capital',
# }


natural = ['Agricultural Water Quality','Agricultural Water Quantity','Biodiversity and Habitat','Ecosystem Services','Forest Change','Green House Emission Per Capita','Land Degradation','Natural Hazard Exposure','Soil Organic Content']
human = ['Access to Agricultural Resources','Food Dietary Diversity','Food Loss','Food Safety','Food Supply Sufficiency','Labor Force Participation Rate','Literacy Rate','Micronutrient Availability','Population Growth Rate','Poverty Population','Protein Quality']
social = ['Agricultural Women Empowerment','Armed Conflict','Community Organizations','Corruption','Dependency on Chronic Food Aid','Food Safety Net Programs','Food Security Policy Commitment','Gender Equality','Nutritional Standards','Political Stability Risk']
financial = ['Access to Diversified Financial Services','Access to Financial Services','Agricultural GDP','Agricultural Production Volatility','Agricultural Trade','Food Price Volatility','Income Inequality','Per Capita GDP']
manufactured = ['Agricultural R&D','Crop Storage Facilities','Disaster Risk Management','Early Warning Measures','Irrigation Infrastructure','KOFGI Globalization Index','Supply Chain Infrastructure','Sustainable Agriculture','Telecommunications']

natural1 = ["Natural Capital",'Agricultural Water Quality','Agricultural Water Quantity','Biodiversity and Habitat','Ecosystem Services','Forest Change','Green House Emission Per Capita','Land Degradation','Natural Hazard Exposure','Soil Organic Content']
human1 = ["Human Capital",'Access to Agricultural Resources','Food Dietary Diversity','Food Loss','Food Safety','Food Supply Sufficiency','Labor Force Participation Rate','Literacy Rate','Micronutrient Availability','Population Growth Rate','Poverty Population','Protein Quality']
social1 = ["Social Capital",'Agricultural Women Empowerment','Armed Conflict','Community Organizations','Corruption','Dependency on Chronic Food Aid','Food Safety Net Programs','Food Security Policy Commitment','Gender Equality','Nutritional Standards','Political Stability Risk']
financial1 = ["Financial Capital",'Access to Diversified Financial Services','Access to Financial Services','Agricultural GDP','Agricultural Production Volatility','Agricultural Trade','Food Price Volatility','Income Inequality','Per Capita GDP']
manufactured1 = ["Manufactured Capital",'Agricultural R&D','Crop Storage Facilities','Disaster Risk Management','Early Warning Measures','Irrigation Infrastructure','KOFGI Globalization Index','Supply Chain Infrastructure','Sustainable Agriculture','Telecommunications']


dataColl = {}
alldata1 = pd.read_csv("FinalData.csv")
alldata1["Year"] = alldata1["Year"].astype("int")
years = range(2012,2023)
for i in years:
    # abc = pd.read_csv(str(i)+'.csv',index_col= 'Country').transpose()
    # dataColl[i] = pd.read_csv(DATA_URL + "\\"+str(i)+'.csv',index_col= 'Country')
    dataColl[i] = alldata1[alldata1["Year"]==i]

org_data=dataColl[2022]
alldata_pivot = alldata1.pivot(index = ["Country","Indicator"],columns="Year",values="value").reset_index()
countries = org_data["Country"].unique()
capitalsOnly = pd.read_csv("finalCapital.csv")

def showOption():
    opts = ['Country','Indicator']
    op = st.sidebar.selectbox('Analysis by:',opts)
    return op

def coloredPlot(df,c1,capital,i):
    fig1 = px.bar(df, x = i,y = df.index,orientation='h', color = "Color",color_discrete_map={"yellow":"Yellow", "green":"green", "red":"red"})
    
    fig1.update_layout(xaxis_range=[0,100],yaxis_title=None, xaxis_title=None,width = 285,height = 500)
    fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    # # fig1['layout']['xaxis'].update(autorange = True)
    fig1.update_xaxes(tickfont=dict(size =10, family = "Arial Black"))
    fig1.update_yaxes(tickfont=dict(size =8,family = "Arial Black"))
    fig1.layout.showlegend = False
    # fig1.update_traces(textposition='outside')
    # c1.subheader(capital) 
    # a1.metric(label="Food System Resilience Score",value=df.loc[df["var_name"]=="Food System Resilience Score",i])
    # if i not in all_factors1.keys():
    #     c1.metric(label=capital+" Capital",value=(np.round(df[i].mean(),1)))
    # else:
    #     c1.subheader(capital)

    c1.subheader(capital)

    c1.plotly_chart(fig1,use_container_width=True)

def linePlotter(df,countrySelect,method = "cvsc"):
#   print(df)
  c = st.columns(3)
  k=0
  if(len(df["Country"].dropna().unique())!=0):
    for i in df["Indicator"].unique():
        df1 = df[df["Indicator"]==i]
        c[k].subheader(i)
        fig = px.line(df1,x="Year", y = "value", color = "Country",markers=True,symbol ="Country")
        fig.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        fig.update_layout(width = 1000)
        fig.update_layout(
    # title="Plot Title",
    # xaxis_title="X Axis Title",
    yaxis_title="Score",
    # legend_title="Legend Title",
    font=dict(
        family="Arial Black",
        size=12,
    )
)
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
        c[k].plotly_chart(fig,use_container_width=True)
        k=k+1
        if k >2:
            k=0

#   if(len(df["Country"].dropna().unique())!=0):
#     for i in df["Country"].dropna().unique():
#         df1=df[df["Country"]==i]
#         print(df1)
#         # d1,d2 = st.columns([1,20])
#         try:
#             st.image("Con_Flags/"+flags[i]+".png",width=50)
#             st.subheader(str.upper(i))
#         except:
#             st.subheader(str.upper(i))
#         # dfm =df1.melt('Year',var_name="Indicators",value_name="Score")
#         # dfm = dfm.replace(all_factors1)
#         fig = px.line(df1,x="Year", y = "value", color = "Indicator",markers=True,symbol ="Indicator")
#         fig.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
#         fig.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
#         fig.update_layout(width = 1000)
#         fig.update_layout(
#     # title="Plot Title",
#     # xaxis_title="X Axis Title",
#     # yaxis_title="Y Axis Title",
#     # legend_title="Legend Title",
#     font=dict(
#         family="Arial Black",
#         size=12,
#     )
# )
#         st.plotly_chart(fig,use_container_width=True)




def linePlot1(df,countrySelect,capital):
    
    ltitle = []
    if capital=="Natural":
        ltitle = natural1
    elif capital=="Human":
        ltitle = human1
    elif capital=="Social":
        ltitle = social1
    elif capital=="Financial":
        ltitle = financial1
    else:
        ltitle = manufactured1
    
    # print(ltitle)

    if(len(countrySelect)!=0):
        for i in countrySelect:
            df1=df[df.index==i]
            print(df1)
            try:
                st.image("Con_Flags/"+flags[i]+".png",width=50)
                st.subheader(str.upper(i))
            except:
                st.subheader(str.upper(i))
            # st.subheader(str.upper(i))
        


            fig2,axs = plt.subplots(figsize=(5,3))
            # fig2,axs = plt.subplots()
            
                    
            # plt.style.use(plt_style)

            dfm =df1.melt('Year',var_name="Capitals",value_name="Score")
            sns.lineplot(x="Year", y="Score", hue = "Capitals",style = "Capitals", markers=True, data = dfm)
            plt.ylabel(None)
            plt.ylim([-5,105])
            plt.legend(ltitle,loc='center left',bbox_to_anchor=(1.1, 0.5),prop={'size': 3})
            plt.show()
            st.pyplot(fig2,use_container_width=True)

def linePlot(df,countrySelect,indicator1):
    print(df)

    # df_ind = df[df["Indicator"]==indicator1]
    
    # print(df_ind)
    try:
        df_ind = df[["Country","Year",indicator1]]
        st.subheader(indicator1)
        fig_ind = px.line(df_ind,x="Year",y=indicator1,color = "Country",markers=True,symbol="Country")
        fig_ind.update_layout(
        yaxis_title="Score",
    legend_title="Country",
    font=dict(
        family="Arial Black",
        size=12,
    ))
        fig_ind.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_ind)
    except:
        st.subheader("No data for "+indicator1 )
    # df.index.name=None
    # c1.write(df)
    c = st.columns(2)
    if(len(countrySelect)!=0):
        # df =df[df.index.isin(countrySelect)]
        # check = df.reset_index().set_index("Year")
        # print(check)
        # c1.write(df)
        # plt.style.use(plt_style)
        # for i in df["Country"].dropna().unique():
        
        # dff = df[df["Indicator"]!=indicator1].copy()
        # dff =df[df["Country"]==i]
        # fd = dff.groupby(["Year","Country"])["value"].mean().reset_index().rename(columns = {"value":"Food Systems Resilience Score"})
        # fd["Natural"] = dff[dff["Indicator"].isin(natural)].groupby(["Year","Country"])["value"].mean().reset_index()["value"]
        # fd["Human"] = dff[dff["Indicator"].isin(human)].groupby(["Year","Country"])["value"].mean().reset_index()["value"]
        # fd["Social"] = dff[dff["Indicator"].isin(social)].groupby(["Year","Country"])["value"].mean().reset_index()["value"]
        # fd["Financial"] = dff[dff["Indicator"].isin(financial)].groupby(["Year","Country"])["value"].mean().reset_index()["value"]
        # fd["Manufactured"] = dff[dff["Indicator"].isin(manufactured)].groupby(["Year","Country"])["value"].mean().reset_index()["value"]
        #     # fd["Country"]=i
        # print(fd)
        k=0
        for j in capitals:
            # if j!="Food Systems Resilience Score":
            try:
                c[k].subheader(j) 
                fig = px.line(df,x="Year",y=j,color = "Country",markers=True)
                fig.update_layout(
                    yaxis_title="Score",
                legend_title="Country",
                font=dict(
                    family="Arial Black",
                    size=12,
                ))
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
                c[k].plotly_chart(fig)
                # k=k+1
                # if k>1:
                #     k=0
            except:
                c[k].write("Not data for "+ j)
            k = k+1
            if k>1:
                k=0

    #         fig1 = px.line(check,x=check.index,y=df.columns[2*i+1],color = "index",markers=True)
    #         fig1.update_layout(
    #             yaxis_title="Score",               
    # legend_title="Country",
    # font=dict(
    #     family="Arial Black",
    #     size=12,
    # ))

    #         c1.plotly_chart(fig)

    #         c2.subheader(str.upper(all_factors1[df.columns[2*i+1]]))
    #         c2.plotly_chart(fig1)


         
def visualizeComp(op,choiceDiff,yearChoice):
    global dataColl
    print(choiceDiff)

    if not (isinstance(yearChoice,list)):
        yearChoice = list(yearChoice)
    yearChoice.reverse()
    print(yearChoice)
    
    if op=="Country":
        countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
        dff = alldata_pivot.loc[alldata_pivot["Country"].isin(countrySelect),:]
        df = dff[["Country","Indicator",yearChoice[0]]]
        df["diff"] = dff[yearChoice[0]] - dff[yearChoice[-1]]

        print(df)

        print('*****')

        traffic(df,index = "Country",yearChoice=yearChoice,extra = "diff")

    elif op =="Countryvs":
        countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
        capital = st.sidebar.selectbox('Capital',['Natural Capital','Human Capital','Social Capital','Financial Capital','Manufactured Capital'])
        indicator1=None
        if capital=="Natural Capital":
            indicator1 = st.sidebar.selectbox("Indicator",natural)
        elif capital=="Human Capital":
            indicator1 = st.sidebar.selectbox("Indicator",human)
        elif capital=="Social Capital":
            indicator1 = st.sidebar.selectbox("Indicator",social)
        elif capital=="Financial Capital":
            indicator1 = st.sidebar.selectbox("Indicator",financial)
        elif capital=="Manufactured Capital":
            indicator1 = st.sidebar.selectbox("Indicator",manufactured)
        else:
            indicator1 = "Food Systems Resilience Score"

        df = alldata1[(alldata1["Indicator"]==indicator1) & (alldata1["Country"].isin(countrySelect))]
        # print(df1.head())

        df_cap = capitalsOnly[capitalsOnly["Country"].isin(countrySelect)].rename(columns = {"Capital":"Indicator"})
        df11 = pd.concat([df,df_cap])
        
        df1 = df11.pivot(index = ["Country","Year"], columns= "Indicator",values="value").reset_index()
        linePlot(df1,countrySelect,indicator1)

    elif op =="Capitals":
        # indexes=[]
        capital = st.sidebar.selectbox("Choose a capital", ["Natural Capital", "Human Capital","Social Capital","Financial Capital","Manufactured Capital"])
        countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
        # print(alldata1.head())
        df = alldata1[alldata1["Country"].isin(countrySelect)].copy()
        if capital=="Natural Capital":
            # indexes = natural
            df = df[df["Indicator"].isin(natural)]
        elif capital=="Human Capital":
            # indexes = human
             df = df[df["Indicator"].isin(human)]
        elif capital=="Social Capital":
            # indexes = social
             df = df[df["Indicator"].isin(social)]

        elif capital=="Financial Capital":
            # indexes = financial
             df = df[df["Indicator"].isin(financial)]
        else:
            # indexes = manufactured
             df = df[df["Indicator"].isin(manufactured)]
        print(df)
        # if "Year" not in indexes:

        #     indexes.append("Year")
        # print(indexes)
        # tempData ={}
        # df = pd.DataFrame()
        # # print(yearChoice)
        # for i in yearChoice:
        #     abc = dataColl[i]
        #     # print(abc)
        #     abc = abc[abc.index.isin(countrySelect)]
        #     abc["Year"]=i
        #     tempData[i]=abc
        #     df =pd.concat([df,tempData[i]])
        # # print(df)
        # df1= df[indexes]
        # print(df1)
        # df1 = df1.reset_index()
        # print(df1.index)
        # linePlot1(df1,countrySelect,capital)
        linePlotter(df,countrySelect,capital)

    elif op =="Change Analysis":
        print("Entered Change Analaysis")
        # st.write("Change Analysis on development..")
        countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
        capital = st.sidebar.selectbox('FSRS/Capital',capitals)
        indicator1=None
        if capital=="Natural Capital":
            indicator1 = st.sidebar.selectbox("Indicator",natural1)
        elif capital=="Human Capital":
            indicator1 = st.sidebar.selectbox("Indicator",human1)
        elif capital=="Social Capital":
            indicator1 = st.sidebar.selectbox("Indicator",social1)
        elif capital=="Financial Capital":
            indicator1 = st.sidebar.selectbox("Indicator",financial1)
        elif capital=="Manufactured Capital":
            indicator1 = st.sidebar.selectbox("Indicator",manufactured1)
        else:
            indicator1 = "Food Systems Resilience Score"
        st.header(indicator1)
        df = pd.DataFrame()
        temp = pd.DataFrame()

        # df = pd.DataFrame()
        print("indicator = "+indicator1)

        index = range(2012,2023)
        if(indicator1 in capitals):
            
            # print(capitalsOnly.head())
            temp = capitalsOnly[capitalsOnly["Capital"]==indicator1].pivot(index = ["Country", "Capital"],columns="Year",values="value").reset_index()
            # print(temp.head())
        else:
            temp = alldata_pivot[alldata_pivot["Indicator"]==indicator1].copy()
            
            # temp["diff"] = temp[yearChoice[0]] - temp[yearChoice[-1]]
            # df = temp[(temp["Capital"]==indicator1)]
        # print(temp.head())
        print(temp[temp["Country"].isin(countrySelect)])
        m=0
        for k in temp.columns:
            # print(k)
            if(index[m]!=2022):
                if not k in ["Country","Capital","Indicator"]:
                    # print(k)
                    temp[str(int(k)+1)] = temp[index[m+1]] - temp[index[m]]
                    temp = temp.drop(columns = [k])
                    m = m+1
        
        df = temp.drop(columns = index[-1]).rename(columns = {"Capital":"Indicator"})
        dataonly = [c for c in df.columns if c not in ["Country","Capital","Indicator",2022]]
        # print(dataonly)
        # print(df[dataonly].cumsum()[df.columns[-1]])
        countryPlot = df[df["Country"].isin(countrySelect)].drop(columns="Indicator").copy().melt("Country", var_name = "Year", value_name="Trend" )
        df["Trend"] = df[dataonly].sum(axis=1,skipna = True)
        df["Color"] = "green"
        df.loc[df["Trend"]<0,"Color"]="red"
        print(df.head())
        c1,c2,c3,c4 = st.columns(4)
        coloredPlot(df.sort_values("Trend",ascending = True).tail(10),c1,"Most Improved Countries","Trend", visType = "Country",present = "2022",height=500,extra = "Trend")
        coloredPlot(df.sort_values("Trend",ascending = False).tail(10),c3,"Most Deteriorated Countries","Trend", visType = "Country",present = "2022",height=500,extra = "Trend")
        # coloredPlot(df.sort_values("Trend",ascending=False).tail(15),c3,"Bottom Ranked Countries","Trend",height=1000,extra = "Trend")
        # coloredPlot(nat,c[k],"Natural Capital",m,visType="Indicator",present = yearChoice[0],extra = "diff")
        print(countryPlot)
        fig = px.line(countryPlot,x="Year",y="Trend",color = "Country",markers=True)
        fig.update_layout(
            yaxis_title="Trend",
        legend_title="Country",
        font=dict(
            family="Arial Black",
            size=12,
        ))
        fig.add_hline(y=0,line_dash = "dash",line_color = "red")
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig)
        



    else:


        vistype = st.sidebar.selectbox("Visualization by:",["Overall", "Income Category","Region"])
        capital = st.sidebar.selectbox('FSRS/Capital',capitals)
        indicator1=None
        if capital=="Natural Capital":
            indicator1 = st.sidebar.selectbox("Indicator",natural1)
        elif capital=="Human Capital":
            indicator1 = st.sidebar.selectbox("Indicator",human1)
        elif capital=="Social Capital":
            indicator1 = st.sidebar.selectbox("Indicator",social1)
        elif capital=="Financial Capital":
            indicator1 = st.sidebar.selectbox("Indicator",financial1)
        elif capital=="Manufactured Capital":
            indicator1 = st.sidebar.selectbox("Indicator",manufactured1)
        else:
            indicator1 = "Food Systems Resilience Score"
        # Year = yearChoice
        df = pd.DataFrame()
        temp = pd.DataFrame()

        # df = pd.DataFrame()
        print("indicator = "+indicator1)


        if(indicator1 in capitals):
            temp = capitalsOnly.pivot(index = ["Country", "Capital"],columns="Year",values="value").reset_index()
            print(temp.head())
            temp["diff"] = temp[yearChoice[0]] - temp[yearChoice[-1]]
            df = temp[(temp["Capital"]==indicator1)]
            print(df.head())

        else:
            temp = alldata_pivot.copy()
            temp["diff"] = alldata_pivot[yearChoice[0]] - alldata_pivot[yearChoice[-1]]
            df = temp[temp["Indicator"]==indicator1].groupby("Country")["diff"].mean().reset_index()
        
        df["Present"]=temp.groupby("Country")[yearChoice[0]].mean().round(1).reset_index()[yearChoice[0]]


        # df["Indicator"] = indicator1
        # df =df.rename(columns={Year:"value"})
        # temp = alldata_pivot.copy()
        # temp["diff"] = alldata_pivot[yearChoice[0]] - alldata_pivot[yearChoice[-1]]
        # print(temp.head())

        # if(indicator1=="Food Systems Resilience Score"):
        #     df = temp[["Country","Indicator","diff"]].groupby("Country")["diff"].mean().reset_index()
        #     df["Present"]=temp.groupby("Country")[yearChoice[0]].mean().reset_index()[yearChoice[0]]
        #     # print(temp.groupby("Country")[yearChoice[0]].mean().reset_index()[yearChoice[0]])
            
        #     # df =df.rename(columns={Year:"value"})
        # elif(indicator1=="Natural Capital"):
        #     df = temp.loc[temp["Indicator"].isin(natural),["Country","Indicator","diff"]].groupby("Country")["diff"].mean().reset_index()
        #     df["Present"]=temp.groupby("Country")[yearChoice[0]].mean().reset_index()[yearChoice[0]]
        #     # df =df.rename(columns={Year:"value"})
        # elif(indicator1=="Human Capital"):
        #     df = temp.loc[temp["Indicator"].isin(human),["Country","Indicator","diff"]].groupby("Country")["diff"].mean().reset_index()
        #     df["Present"]=temp.groupby("Country")[yearChoice[0]].mean().reset_index()[yearChoice[0]]
        #     # df =df.rename(columns={Year:"value"})
        # elif(indicator1=="Social Capital"):
        #     df = temp.loc[temp["Indicator"].isin(social),["Country","Indicator","diff"]].groupby("Country")["diff"].mean().reset_index()
        #     df["Present"]=temp.groupby("Country")[yearChoice[0]].mean().reset_index()[yearChoice[0]]
        #     # df =df.rename(columns={Year:"value"})
        # elif(indicator1=="Financial Capital"):
        #     df = temp.loc[temp["Indicator"].isin(financial),["Country","Indicator","diff"]].groupby("Country")["diff"].mean().reset_index()
        #     # df =df.rename(columns={Year:"value"})
        #     df["Present"]=temp.groupby("Country")[yearChoice[0]].mean().reset_index()[yearChoice[0]]
        # elif(indicator1=="Manufactured Capital"):
        #     df = temp.loc[temp["Indicator"].isin(manufactured),["Country","Indicator","diff"]].groupby("Country")["diff"].mean().reset_index()
        #     # df =df.rename(columns={Year:"value"})
        #     df["Present"]=temp.groupby("Country")[yearChoice[0]].mean().reset_index()[yearChoice[0]]
        # else:
        #     df = temp[temp["Indicator"]==indicator1].groupby("Country")["diff"].mean().reset_index()
        #     df["Present"]=temp.groupby("Country")[yearChoice[0]].mean().reset_index()[yearChoice[0]]
            # df =df.rename(columns={Year:"value"})
        
        df = df.rename(columns={"diff":"value"})
        # df["Indicator"] = indicator1
        # df =df.rename(columns={Year:"value"})
        # dff = df.copy()
        # print(dff)
        # df = dff[["Country","Indicator",yearChoice[0]]]
        # df["value"] = dff[yearChoice[0]] - dff[yearChoice[-1]]
        # original = df[["CountyearChoice[0]]]

        # df = dataColl[yearChoice[0]].subtract(dataColl[yearChoice[1]])[[all_factors[indicator1]]]
        print(df.head())
        # df = df[df.index.isin(countrySelect)].transpose()
        # original = dataColl[yearChoice[0]][dataColl[yearChoice[0]].index.isin(countrySelect)].transpose()
        # original = dataColl[yearChoice[0]][[all_factors[indicator1]]]
        # print(original)
        # indSelect1 = st.sidebar.multiselect('Select indicator(s)',all_factors.keys())
        # # trans_data=pd.read_csv(DATA_URL + "\\"+str(yearChoice)+'.csv',index_col= 'Country').transpose()
        # indSelect = [all_factors[i] for i in indSelect1]
        # print("choice of year = " + str(yearChoice))
        # trans_data=dataColl[yearChoice]
        # print(trans_data)
        # print(all_factors[indicator1])
        # df1 = trans_data.loc[:,[all_factors[indicator1]]]
        # print(yearChoice)
        # print("IF ELSE")
        # print(df1.head())

        showPlot(df,index='country',visType=vistype,indicator=indicator1,present = df[["Present"]])

def traffic(df,index = "Country",visType="Time",check="nice",yearChoice=None,extra = "value"):
    print("Entered Traffic" + str(yearChoice))
    # print(df)
    k=0
    
    for i in df[index].unique():
        dff = df[df[index]==i]
        # print(present)
        # d1,d2 = st.columns([1,15])
        # try:
        #     c[k].image("Con_Flags/"+flags[i]+".png",width=50)
        #     c[k].subheader(str.upper(i))
        # except:
        #     c[k].subheader(str.upper(i))
        
        # c[k].metric("Food Systems Resilience Score", np.round(dff[yearChoice[0]].mean(),2),delta = np.round(float(dff["diff"].mean()),1))

        try:
            st.image("Con_Flags/"+flags[i]+".png",width=50)
            st.subheader(str.upper(i))
        except:
            st.subheader(str.upper(i))
        
        st.metric("Food Systems Resilience Score", np.round(dff[yearChoice[0]].mean(),2),delta = np.round(float(dff["diff"].mean()),1))
        c = st.columns(5)
        # c1,c2,c3,c4,c5 = st.columns(5)
        # colored = dff.sort_values(yearChoice[0],ascending=True).copy()
        colored = dff.copy()
        m="diff"
        colored["Color"] = "green"
        colored.loc[colored[m]<0,"Color"] = "red"
        # colored.loc[(colored[i]>=40) & (colored[i]<80),"Color"]= "yellow"
        # colored.index = colored.index.map(all_factors1)

        # print(colored)
        
        nat = colored[colored["Indicator"].isin(natural)].sort_values("Indicator")
        hum =colored[colored["Indicator"].isin(human)].sort_values("Indicator")
        soc = colored[colored["Indicator"].isin(social)].sort_values("Indicator")
        fin = colored[colored["Indicator"].isin(financial)].sort_values("Indicator")
        man = colored[colored["Indicator"].isin(manufactured)].sort_values("Indicator")

        print(nat)

        # present_nat = present[present.index.isin(natural)]
        # present_hum = present[present.index.isin(human)]
        # present_soc = present[present.index.isin(social)]
        # present_fin = present[present.index.isin(financial)]
        # present_man = present[present.index.isin(manufactured)]
        # print(nat)
        
        # coloredPlot(nat,c[k],"Natural Capital",m,visType="Indicator",present = yearChoice[0],extra = "diff")
        # coloredPlot(hum,c[k],"Human Capital",m,visType="Indicator",present = yearChoice[0],extra = "diff")
        # coloredPlot(soc,c[k],"Social Capital",m,visType="Indicator",present = yearChoice[0],extra = "diff")
        # coloredPlot(fin,c[k],"Financial Capital",m,visType="Indicator",present = yearChoice[0],extra = "diff")
        # coloredPlot(man,c[k],"Manufactured Capital",m,visType="Indicator",present = yearChoice[0],extra = "diff")
        
        coloredPlot(nat,c[0],"Natural Capital",m,visType="Indicator",present = yearChoice[0],extra = "diff")
        coloredPlot(hum,c[1],"Human Capital",m,visType="Indicator",present = yearChoice[0],extra = "diff")
        coloredPlot(soc,c[2],"Social Capital",m,visType="Indicator",present = yearChoice[0],extra = "diff")
        coloredPlot(fin,c[3],"Financial Capital",m,visType="Indicator",present = yearChoice[0],extra = "diff")
        coloredPlot(man,c[4],"Manufactured Capital",m,visType="Indicator",present = yearChoice[0],extra = "diff")
        k=k+1
        if k >4:
            k=0

def coloredPlot(df,c1,capital,i,visType=None,present="Present",height =500,extra = "diff"):
    # print(i)
    # print(df.head())
    # df = df.sort_values(visType,ascending = True)
    df = df.dropna()
    if not df.empty:
        df = df.replace({0:0.1})
        df[i] = np.round(df[i],1)
        fig1 = px.bar(df, x = i,y = visType,orientation='h', text = i,color = "Color",color_discrete_map={"yellow":"Yellow", "green":"green", "red":"red"})
        # fig1.update_layout(xaxis=dict(type='category'))
        fig1.update_layout(xaxis_range=[-100,100],yaxis_title=None, xaxis_title=None,height = height)
        fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
        fig1.update_layout(xaxis_range = [-100,100])
        fig1.update_xaxes(tickfont=dict(size =10, family = "Arial Black"))
        fig1.update_yaxes(tickfont=dict(size =10,family = "Arial Black"))
        fig1.layout.showlegend = False
        fig1.update_traces(textposition = "auto")
        
        # fig1.update_traces(textposition='outside')
        # c1.subheader(capital) 
        # a1.metric(label="Food System Resilience Score",value=df.loc[df["var_name"]=="Food System Resilience Score",i])
        # if i not in all_factors1.keys():
        #     if visType!="Time":
        #         c1.metric(label=capital+" Capital",value=(np.round(df[i].mean(),1)))
        #     else:
        #         c1.metric(label=capital+" Capital",value=np.round(present[i].mean(),2),delta = np.round(df[i].mean(),1))

        # else:
        #     c1.subheader(capital)
        print(df.head(3))
        value = nan
        delta = nan
        try:
            value=np.round(df[present].mean(),2)
            delta = np.round(df[extra].mean(),1)
        except:
            pass

        c1.metric(label=capital,value=value,delta = delta)
        # c1.subheader(capital)
        c1.plotly_chart(fig1,use_container_width=True)
    else:
        c1.write("No data for "+capital)


def showPlot(df,index = "Country",visType="Des",indicator="nice",present=pd.DataFrame()):
    
    st.subheader(indicator)

    df11 =df.merge(incomeCat,on="Country",how="left")
    print(df11["Country"].unique())

    print("Income = "+ str(len(df11["Income Group"].unique())))
    print("region = "+ str(len(df11["Region"].unique())))
    # c = []
    # c = st.columns(4)


        

    if visType == "Income Category":
        c = st.columns(4)
        k=0
        for j in df11["Income Group"].dropna().unique():
            print(j)
            print(df11.head())
        
            fd = df11[df11["Income Group"]==j].sort_values("value",ascending=True)
            fd.index = fd["Country"]
            fd["Color"]="green"
            fd.loc[fd["value"]<0,"Color"] = "red"
            # fd.loc[(fd["value"]>=40) & (fd["value"]<80),"Color"]= "yellow"
            # print(c)
            coloredPlot(fd,c[k],j,"value",height = 1000,extra="value")
            k=k+1
            if k>3:
                k=0
    elif visType == "Region":
        k=0
        c = st.columns(4)
        for j in df11["Region"].dropna().unique():
        
            fd = df11[df11["Region"]==j].sort_values("value",ascending=True)
            fd.index = fd["Country"]
            fd["Color"]="green"
            fd.loc[fd["value"]<0,"Color"] = "red"
            # fd.loc[(fd["value"]>=40) & (fd["value"]<80),"Color"]= "yellow"
            # print(c)
            coloredPlot(fd,c[k],j,"value",height=1000,extra = "value")
            k=k+1

            if(k>3):
                k=0
    else:
        c1,c2,c3,c4 = st.columns(4)
        fd = df.dropna()
        print(fd.head())
        fd.index = fd["Country"]
        fd["Color"]="green"
        fd.loc[fd["value"]<0,"Color"] = "red"
        # fd = fd.sort_values("value",ascending=True)
        # bottom = fd.sort_values("value",ascending = False).tail(15)
        # print(bottom.sort_values("value",ascending=True))
        # print(c)
        coloredPlot(fd.sort_values("value",ascending = True).tail(15),c1,"Top Ranked Countries","value",height=1000,extra = "value")
        coloredPlot(fd.sort_values("value",ascending=False).tail(15),c3,"Bottom Ranked Countries","value",height=1000,extra = "value")



def app():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
    st.sidebar.subheader("LEGEND")
    style_text=""
    for i in range(2):
        colors = ['red','green']
        legend = ['Improvement', 'Deterioration' ]
        style_text+= "<div><div class='rectangle {}'></div> {}</div>".format(colors[i],legend[i])
    # print(style_text)
    st.sidebar.markdown(style_text,unsafe_allow_html=True)
    yearChoice = [*range(2012,2023)]
    choiceDiff =  st.sidebar.selectbox('Select a type',["Year-on-Year Analysis", "Change Analysis","Country vs Country", "Capitals"])
    if choiceDiff=="Year-on-Year Analysis":
        yearChoice = st.sidebar.slider("Choose Year Range",2012,2022,(2012,2022))
        #  in ["1-year Analysis","5-Year Analysis", "YTD Analysis"]:
        op =showOption()
    elif choiceDiff== "Country vs Country":
        op = "Countryvs"
    else:
        op = choiceDiff
    visualizeComp(op,choiceDiff,yearChoice)
